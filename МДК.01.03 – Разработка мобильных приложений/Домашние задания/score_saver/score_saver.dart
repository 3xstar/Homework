import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class CounterWithSaveApp extends StatefulWidget {
  const CounterWithSaveApp({super.key});

  @override
  State<CounterWithSaveApp> createState () => _CounterWithSaveAppState();
}

class _CounterWithSaveAppState extends State<CounterWithSaveApp> {
  int _counter = 0;

  Future<void> _loadCounter() async {
    final prefs = await SharedPreferences.getInstance();
    final int? savedCounter = prefs.getInt('counter');

    print('Загрузка: сохранённое значение = $savedCounter');

    setState((){
      _counter = savedCounter ?? 0;
    });

    print('Установлено значение: $_counter');
  }

  @override
  void initState(){
    super.initState();
    _loadCounter();
  }

  Future<void> _saveCounter() async{
    final prefs = await SharedPreferences.getInstance();
    await prefs.setInt('counter', _counter);
    print('Сохранено: $_counter');
  }

  void _incrementCounter(){
    setState(() {
      _counter++;      
    });
    _saveCounter();
  }

  @override
  Widget build(BuildContext context){
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.cyan,
        appBar: AppBar(title: Text("Локальный счетчик", style: TextStyle())),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Text('Значение счетчика', style: TextStyle(color: Colors.white, fontSize: 25)),
              Text('$_counter', style: TextStyle(fontSize: 50)),
              ElevatedButton(
              onPressed: _incrementCounter,
              child: Text('Увеличить', style: TextStyle(fontSize: 20),),
              ),
            ],
          ),
        ),
      ),
    );
  }
}