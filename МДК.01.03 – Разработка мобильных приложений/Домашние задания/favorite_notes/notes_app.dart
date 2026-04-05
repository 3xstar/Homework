import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:image_picker/image_picker.dart';
// flutter pub add image_picker

// ==================== ТОЧКА ВХОДА ====================
class NotesDB extends StatelessWidget {
  const NotesDB({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: const NotesDBHome(),
    );
  }
}

// ==================== ГЛАВНЫЙ ЭКРАН ====================
class NotesDBHome extends StatefulWidget {
  const NotesDBHome({super.key});

  @override
  State<NotesDBHome> createState() => _NotesDBHomeState();
}

class _NotesDBHomeState extends State<NotesDBHome> {
  int _currentIndex = 0;
  late final List<Widget> _screens;

  @override
  void initState() {
    super.initState();
    _screens = const [AllNotesScreen(), FavoritesNotesScreen(), ProfileScreen()];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) => setState(() => _currentIndex = index),
        type: BottomNavigationBarType.fixed,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.list), label: 'Все заметки'),
          BottomNavigationBarItem(icon: Icon(Icons.star), label: 'Избранное'),
          BottomNavigationBarItem(icon: Icon(Icons.person_2), label: 'Профиль'),
        ],
      ),
    );
  }
}

class AllNotesScreen extends StatefulWidget {
  const AllNotesScreen({super.key});

  @override
  State<AllNotesScreen> createState() => _AllNotesScreenState();
}

class _AllNotesScreenState extends State<AllNotesScreen> {
  List<dynamic> _tasks = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadTasks();
  }

  // Загрузка заметок
  Future<void> _loadTasks() async {
    setState(() => _isLoading = true);
    try {
      final response = await http.post(
        Uri.parse('http://localhost/tasks_2.php'),
        body: {'action': 'read'},
      );
      final data = jsonDecode(response.body);
      setState(() {
        _tasks = data['tasks'] ?? [];
        _isLoading = false;
      });
    } catch (e) {
      setState(() => _isLoading = false);
      debugPrint('Ошибка: $e');
    }
  }

  // Добавление
  Future<void> _createTask(String title) async {
    await http.post(
      Uri.parse('http://localhost/tasks_2.php'),
      body: {'action': 'create', 'title': title},
    );
    _loadTasks();
  }

  // Удаление
  Future<void> _deleteTask(int id) async {
    await http.post(
      Uri.parse('http://localhost/tasks_2.php'),
      body: {'action': 'delete', 'id': id.toString()},
    );
    _loadTasks();
  }

  // Редактирование
  Future<void> _updateTask(int id, String title) async {
    await http.post(
      Uri.parse('http://localhost/tasks_2.php'),
      body: {'action': 'update', 'id': id.toString(), 'title': title},
    );
    _loadTasks();
  }

  // добавление в избранное
  Future<void> _favoriteTask(int id) async {
    await http.post(
      Uri.parse('http://localhost/tasks_2.php'),
      body: {'action': 'toggle_favorite', 'id': id.toString()},
    );
    _loadTasks();
  }

  // Диалог добавления/редактирования
  void _showTaskDialog({int? id, String? title}) {
    final controller = TextEditingController(text: title ?? '');
    showDialog(
      context: context,
      builder: (_) => AlertDialog(
        title: Text(id == null ? 'Новая заметка' : 'Редактировать'),
        content: TextField(
          controller: controller,
          autofocus: true,
          decoration: const InputDecoration(
            labelText: 'Название',
            border: OutlineInputBorder(),
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Отмена'),
          ),
          TextButton(
            onPressed: () {
              Navigator.pop(context);
              if (id == null) {
                _createTask(controller.text);
              } else {
                _updateTask(id, controller.text);
              }
            },
            child: const Text('OK'),
          ),
        ],
      ),
    );
  }

  // Подтверждение удаления
  void _confirmDelete(int id, String title) {
    showDialog(
      context: context,
      builder: (_) => AlertDialog(
        title: const Text('Удалить?'),
        content: Text('"$title"'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Отмена'),
          ),
          TextButton(
            onPressed: () {
              Navigator.pop(context);
              _deleteTask(id);
            },
            child: const Text('Удалить', style: TextStyle(color: Colors.red)),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Задачи'),
        actions: [
          IconButton(
            icon: const Icon(Icons.add),
            onPressed: () => _showTaskDialog(),
          ),
        ],
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : _tasks.isEmpty
          ? const Center(child: Text('Нет заметок'))
          : ListView.builder(
              itemCount: _tasks.length,
              itemBuilder: (context, index) {
                final task = _tasks[index];
                final id = int.parse(task['id'].toString());
                return ListTile(
                  title: Text(task['title']),
                  subtitle: Text('ID: ${task['id']}'),
                  onTap: () => _showTaskDialog(id: id, title: task['title']),
                  trailing: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      IconButton(
                        icon: Icon(
                          // Если 1 - желтая закрашенная, если 0 - серая контурная
                          (task['is_favorite'] == 1 || task['is_favorite'] == '1') 
                              ? Icons.star 
                              : Icons.star_border,
                          color: (task['is_favorite'] == 1 || task['is_favorite'] == '1') 
                              ? Colors.amber 
                              : Colors.grey,
                        ),
                        onPressed: () => _favoriteTask(id), 
                        ),
                        IconButton(
                          icon: const Icon(Icons.delete, color: Colors.red),
                          onPressed: () => _confirmDelete(id, task['title']),
                        ),
                      ],
                    ),
                  );
                },
              ),
            );
  }
}

class FavoritesNotesScreen extends StatefulWidget {
  const FavoritesNotesScreen({super.key});

  @override
  State<FavoritesNotesScreen> createState() => _FavoritesNotesScreenState();
}

class _FavoritesNotesScreenState extends State<FavoritesNotesScreen> {
  List<dynamic> _tasks = [];
  bool _isLoading = true;

  @override 
  void initState() {
    super.initState();
    _loadTasks();
  }

  Future<void> _loadTasks() async {
    setState(() => _isLoading = true);
    try {
      final response = await http.post(
        Uri.parse('http://localhost/tasks_2.php'),
        body: {'action': 'read', 'favorite': 'true'},
      );
      final data = jsonDecode(response.body);
      setState(() {
        _tasks = data['tasks'] ?? [];
        _isLoading = false;
      });
    } catch (e) {
      setState(() => _isLoading = false);
      debugPrint('Ошибка: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Избранное')),
      body: _isLoading ? Center(child: CircularProgressIndicator()) : _tasks.isEmpty ? Center(child: Text('Нет избранных заметок')) 
      : ListView.builder(
        itemCount: _tasks.length,
        itemBuilder: (context, index) {
          final task = _tasks[index];
          return ListTile(
            leading: Icon(Icons.star, color: Colors.amber,),
            title: Text(task['title']),
            subtitle: Text('ID: ${task['id']}'),
          );
        },
      )
    );
  }
}

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  String _name = '';
  String _avatar = '';
  bool _isLoading = true;

  @override 
  void initState() {
    super.initState();
    _loadProfile();
  }

  Future<void> _loadProfile() async {
    final response = await http.post(
      Uri.parse('http://localhost/profile.php'),
      body: {'action': 'get_profile'},
    );
    final data = jsonDecode(response.body);
    setState(() {
      _name = data['user']['name'] ;
      _avatar = data['user']['avatar'];
      _isLoading = false;
    });
  }

  Future<void> _pickAvatar() async {
    final picker = ImagePicker();
    final image = await picker.pickImage(source: ImageSource.gallery);

    if (image != null) {
      var request = http.MultipartRequest(
        'POST',
        Uri.parse('http://localhost/profile.php'),
      );  
      request.fields['action'] = 'upload_avatar';
      request.files.add(await http.MultipartFile.fromPath('avatar', image.path));

      final response = await request.send();
      if (response.statusCode == 200) {
        _loadProfile();
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('обновлено')),
          );
        }
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar:  AppBar(title: Text('Профиль')),
      body: _isLoading ? Center(child: CircularProgressIndicator()) 
      : Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircleAvatar(
              radius: 100,
              backgroundImage: NetworkImage('http://localhost/notes_avatars/$_avatar'),
            ),
            Text(_name),
            TextButton(onPressed: _pickAvatar, child: Text('изменить аватарку')),
          ],
        ),
      )
    );
  }
}
