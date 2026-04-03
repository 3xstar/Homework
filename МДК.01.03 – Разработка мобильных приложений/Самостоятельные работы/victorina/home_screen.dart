import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'quiz_screen.dart';

class VictorinaHome extends StatefulWidget {
  const VictorinaHome({super.key});

  @override
  State<VictorinaHome> createState() => _VictorinaHomeState();
}

class _VictorinaHomeState extends State<VictorinaHome>{
  int _bestScore = 0;

  @override
  void initState() {
    super.initState();
    _loadBestScore();
  }

  Future<void> _loadBestScore() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _bestScore = prefs.getInt('best_score') ?? 0;
    });
  }

  Future<void> _saveBestScore(int score) async {
    final prefs = await SharedPreferences.getInstance();
    final bestScore = prefs.getInt('best_score') ?? 0;
    if (score > bestScore) {
      await prefs.setInt('best_score', score);
      setState(() => _bestScore = score);
    }
  }

  Future<void> _resetBestScore() async{
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('best_score');
    setState((){
      _bestScore = 0;
    });
  }
 
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Викторина')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.quiz, size: 100, color: Colors.blue),
            const SizedBox(height: 32),
            const Text('Викторина', style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold)),
            const SizedBox(height: 16),
            Text('Рекорд: $_bestScore', style: const TextStyle(fontSize: 20)),
            const SizedBox(height: 32),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (_) => QuizScreen(onFinish: _saveBestScore),
                ),
              );
              },
              child: const Padding(
                padding: EdgeInsets.all(12.0),
                child: Text('Начать', style: TextStyle(fontSize: 16)),
              ),
            ),
            const SizedBox(height: 10),
            TextButton(
              onPressed: _resetBestScore,
              child: const Text('Сбросить рекорд'),
            ),
          ],
        ),
      ),
    );
  }
}