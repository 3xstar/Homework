import 'package:flutter/material.dart';

class CounterWidget extends StatefulWidget {
  
  const CounterWidget({super.key});

  @override
  State<CounterWidget> createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
  int _counter = 0;
  bool _isLiked = false;
  int _likeCount = 0;

  void _toggleLike() {
    setState(() {
      _isLiked = !_isLiked;
      _likeCount = _isLiked ? 1 : 0;
    });
  }

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }
  @override
  Widget build(BuildContext context){
  return MaterialApp(
    debugShowCheckedModeBanner: false,
    home: Scaffold(
      appBar: AppBar(
        title: const Text('Счетчик'),
        backgroundColor: Colors.cyan,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Значение счетчика: ',
              style: TextStyle(fontSize: 20),
            ),
            const SizedBox(height: 10),

            Text(
              '$_counter',
              style: const TextStyle(fontSize: 48, fontWeight: FontWeight.bold),
            ),
            IconButton(onPressed: _toggleLike,
              icon: Icon(
              _isLiked ? Icons.favorite : Icons.favorite_border,
              color: _isLiked ? Colors.red : Colors.grey,
              size: 30,
            ),
            ),
            const SizedBox(width: 8),
            Text(
              '$_likeCount',
              style: TextStyle(
                color: _isLiked ? Colors.red : Colors.grey,
                fontWeight: FontWeight.bold,
                fontSize: 20,
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        backgroundColor: Colors.cyan,
        child: const Icon(Icons.add),
      ),
    ),
  );
}
}