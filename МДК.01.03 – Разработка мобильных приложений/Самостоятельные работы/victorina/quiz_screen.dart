import 'package:flutter/material.dart';
import 'dart:math';

class QuizScreen extends StatefulWidget {

  final Function(int) onFinish;

  const QuizScreen({super.key, required this.onFinish});

  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen>
{
  final List<Map<String, dynamic>> _questions = [
  {
    'question': 'Какова цена взрослой жизни?',
    'options': ['пачка кириешек', 'Берлин', 'доширак', 'отсутствие нервов'],
    'correct': 3,
  },
  {
    'question': 'Какой преподаватель является самым лучшим?',
    'options': ['Захар', 'Никита', 'Андрей', 'Андрей'],
    'correct': 1,
  },
    {
    'question': 'Сколько будет 2 + 2 * 2?',
    'options': ['6', '8', '4', '10'],
    'correct': 0,  // Правильный ответ: индекс 0 = '6'
  },
  {
    'question': 'Какой язык используется во Flutter?',
    'options': ['Java', 'Kotlin', 'Dart', 'Swift'],
    'correct': 2,  // Dart
  },
  {
    'question': 'Что возвращает setState()?',
    'options': ['void', 'Future', 'Widget', 'bool'],
    'correct': 0,  // void
  },
  ];

  @override
  void initState() {
    super.initState();
    _questions.shuffle(Random());
  }

  int _currentQuestion = 0;
  int _score = 0;
  bool _answered = false;
  bool _showResult = false;
  
  void _restart() {
    setState(() {
      _currentQuestion = 0;  // Сбрасываем номер вопроса
      _score = 0;            // Сбрасываем счёт
      _answered = false;     // Разблокируем кнопки
      _showResult = false;   // Скрываем экран результата
      _questions.shuffle(Random());  // Перемешиваем вопросы заново!
    });
  }

  void _selectAnswer(int index) {
    if (_answered) return;  // Нельзя выбрать дважды

    // Считаем очки
    if (index == _questions[_currentQuestion]['correct']) {
      _score++;
    }

    // Экран становится неактивным
    setState(() => _answered = true);

  // Через 0.5 секунды — следующий вопрос
  Future.delayed(const Duration(milliseconds: 500), () {
    if (_currentQuestion < _questions.length - 1) {
      setState(() {
        _currentQuestion++;
        _answered = false;
      });
    } else {
      setState(() => _showResult = true);
    }
    });
  }

  @override
  Widget build(BuildContext context) {
    final question = _questions[_currentQuestion];
    final options = List<String>.from(question['options']);
    if (_showResult) {
      widget.onFinish(_score);  // Вызываем функцию сохранения рекорда
      return Scaffold(
      appBar: AppBar(title: const Text('Результат')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.emoji_events, size: 100, color: Colors.amber),
            const SizedBox(height: 32),
            Text(
              '$_score из ${_questions.length}',
              style: const TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 16),
            Text(
              _score == _questions.length
                  ? 'Идеально!'
                  : _score > _questions.length / 2
                      ? 'Неплохо '
                      : 'Попробуй ещё раз ',
              style: const TextStyle(fontSize: 18),
            ),
            const SizedBox(height: 32),
            ElevatedButton(
              onPressed: _restart,
              child: const Text('Играть снова'),
            ),
          ],
        ),
      ),
    );
  }  // Экран с результатом

  return Scaffold(
    appBar: AppBar(
      title: Text('Вопрос ${_currentQuestion + 1}/${_questions.length}'),
    ),
    body: IgnorePointer(
      ignoring: _answered,
      child: AnimatedOpacity(
        opacity: _answered ? 0.5 : 1.0,
        duration: const Duration(milliseconds: 200),
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 32),
              Text(
                question['question'],
                style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 32),
              ...options.map((option) => Padding(
                padding: const EdgeInsets.only(bottom: 12.0),
                child: ElevatedButton(
                  onPressed: () => _selectAnswer(options.indexOf(option)),
                  style: ElevatedButton.styleFrom(
                  padding: const EdgeInsets.all(16.0)),
                  child: Text(option, style: const TextStyle(fontSize: 16)),
                ),
              )).toList(),
            ],
          ),
        ),
      ),
    ),
  );
}
}

