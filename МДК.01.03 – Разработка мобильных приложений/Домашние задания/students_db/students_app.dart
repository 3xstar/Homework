import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class LocalhostApp extends StatefulWidget {
  const LocalhostApp({super.key});

  @override
  State<LocalhostApp> createState() => _LocalhostAppState();
}

class _LocalhostAppState extends State<LocalhostApp> {
  List<dynamic> _students = [];
  bool _isLoading = true;
  
  // === НОВОЕ: Переменная для сортировки ===
  // Варианты: 'name_asc' (А-Я), 'name_desc' (Я-А), 'score_desc' (5.0 -> 2.0), 'score_asc' (2.0 -> 5.0)
  String _sortBy = 'name_asc'; 

  @override
  void initState() {
    super.initState();
    _loadStudents();
  }

  Future<void> _loadStudents() async {
    try {
      final response = await http.post(
        Uri.parse('http://localhost/students.php'),
        body: {
          'action': 'read', 
          'sort': _sortBy, // === ОТПРАВЛЯЕМ ПАРАМЕТР СОРТИРОВКИ НА СЕРВЕР ===
        },
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);

        if (data['success'] == true) {
          setState(() {
            _students = data['data'] ?? [];
            _isLoading = false;
          });
        } else {
          print('Ошибка сервера: $data');
          setState(() => _isLoading = false);
        }
      } else {
        print('Ошибка HTTP: ${response.statusCode}');
        setState(() => _isLoading = false);
      }
    } catch (e) {
      print('Ошибка подключения: $e');
      setState(() => _isLoading = false);
    }
  }

  // === НОВОЕ: Переключение сортировки ===
  void _toggleSort() {
    setState(() {
      if (_sortBy == 'name_asc') {
        _sortBy = 'name_desc'; // А-Я -> Я-А
      } else if (_sortBy == 'name_desc') {
        _sortBy = 'score_desc'; // Я-А -> Оценка (высший сначала)
      } else if (_sortBy == 'score_desc') {
        _sortBy = 'score_asc'; // Оценка (высший) -> Оценка (низший)
      } else {
        _sortBy = 'name_asc'; // Оценка (низший) -> А-Я (круг замкнулся)
      }
    });
    _loadStudents(); // Перезагружаем данные с новым параметром
  }

  Future<void> _createStudent(String name, String groupNum, double averageScore) async {
    await http.post(
      Uri.parse('http://localhost/students.php'),
      body: {
        'action': 'create',
        'name': name,
        'group_num': groupNum,
        'average_score': averageScore.toString(),
      },
    );
    _loadStudents();
  }

  Future<void> _updateStudent(String name, String groupNum, double averageScore, int id) async {
    await http.post(
      Uri.parse('http://localhost/students.php'),
      body: {
        'action': 'update',
        'name': name,
        'group_num': groupNum,
        'average_score': averageScore.toString(),
        'id': id.toString(),
      },
    );
    _loadStudents();
  }

  Future<void> _deleteStudent(int id) async {
    await http.post(
      Uri.parse('http://localhost/students.php'),
      body: {
        'action': 'delete',
        'id': id.toString(),
      },
    );
    _loadStudents();
  }

  void _showTaskDialog({
    int? id,
    String? name,
    String? group_num,
    dynamic average_score,
  }) {
    final nameController = TextEditingController(text: name ?? '');
    final groupController = TextEditingController(text: group_num ?? '');
    
    String scoreText = '';
    if (average_score != null) {
      scoreText = average_score.toString();
    }
    final scoreController = TextEditingController(text: scoreText);

    showDialog(
      context: context,
      builder: (_) => AlertDialog(
        title: Text(id == null ? 'Новый студент' : 'Редактировать'),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            TextField(
              controller: nameController,
              autofocus: true,
              decoration: const InputDecoration(
                labelText: 'Имя',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: groupController,
              decoration: const InputDecoration(
                labelText: 'Группа',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: scoreController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(
                labelText: 'Средний балл',
                border: OutlineInputBorder(),
              ),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Отмена'),
          ),
          TextButton(
            onPressed: () {
              Navigator.pop(context);
              double newScore = double.tryParse(scoreController.text) ?? 0.0;

              if (id == null) {
                _createStudent(nameController.text, groupController.text, newScore);
              } else {
                _updateStudent(nameController.text, groupController.text, newScore, id);
              }
            },
            child: const Text('OK'),
          ),
        ],
      ),
    );
  }

  void _confirmDelete(int id, String name) {
    showDialog(
      context: context,
      builder: (_) => AlertDialog(
        title: const Text('Удалить?'),
        content: Text('"$name"'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Отмена'),
          ),
          TextButton(
            onPressed: () {
              Navigator.pop(context);
              _deleteStudent(id);
            },
            child: const Text('Удалить', style: TextStyle(color: Colors.red)),
          ),
        ],
      ),
    );
  }

  Color _getScoreColor(dynamic score) {
    // Безопасное преобразование в double
    double value = 0.0;
    if (score is double) {
      value = score;
    } else if (score is int) {
      value = score.toDouble();
    } else if (score is String) {
      value = double.tryParse(score) ?? 0.0;
    }

    if (value >= 4.5) {
      return Colors.green;
    } else if (value >= 3.0) {
      return Colors.orange;
    } else {
      return Colors.red;
    }
  }

  @override
  Widget build(BuildContext context) {
    // Определяем иконку и текст подсказки в зависимости от режима
    IconData sortIcon;
    String sortTooltip;

    if (_sortBy == 'name_asc') {
      sortIcon = Icons.sort_by_alpha; // А-Я
      sortTooltip = 'Сортировка: Имя (А → Я)';
    } else if (_sortBy == 'name_desc') {
      sortIcon = Icons.sort_by_alpha; // Я-А (можно добавить зеркальную иконку, но стандартной нет)
      sortTooltip = 'Сортировка: Имя (Я → А)';
    } else if (_sortBy == 'score_desc') {
      sortIcon = Icons.trending_up; // Высокий балл сверху
      sortTooltip = 'Сортировка: Оценка (Высший → Низший)';
    } else {
      sortIcon = Icons.trending_down; // Низкий балл сверху
      sortTooltip = 'Сортировка: Оценка (Низший → Высший)';
    }

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Студенты'),
          actions: [
            // === НОВОЕ: Кнопка сортировки ===
            IconButton(
              onPressed: _toggleSort,
              icon: Icon(sortIcon),
              tooltip: sortTooltip,
            ),
            // Кнопка добавления
            IconButton(
              onPressed: () => _showTaskDialog(),
              icon: const Icon(Icons.add),
            ),
          ],
        ),
        body: _isLoading
            ? const Center(child: CircularProgressIndicator())
            : ListView.builder(
                itemCount: _students.length,
                itemBuilder: (context, index) {
                  final student = _students[index];

                  final int id = student['id'] is int
                      ? student['id']
                      : int.tryParse(student['id'].toString()) ?? 0;
                  
                  final String name = student['name']?.toString() ?? 'Без имени';
                  final String group = student['group_num']?.toString() ?? '';
                  final dynamic score = student['average_score'];

                  return ListTile(
                    title: Text(name),
                    subtitle: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text('Группа: $group'),
                        Text(
                          'Балл: $score', 
                          style: TextStyle(
                            color: _getScoreColor(score),
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                    onTap: () => _showTaskDialog(
                      id: id,
                      name: name,
                      group_num: group,
                      average_score: score,
                    ),
                    trailing: IconButton(
                      onPressed: () => _confirmDelete(id, name),
                      icon: const Icon(Icons.delete, color: Colors.red),
                    ),
                  );
                },
              ),
      ),
    );
  }
}