import 'package:flutter/material.dart';
import 'package:getwidget/getwidget.dart';

class EmailApp extends StatelessWidget{
  const EmailApp({super.key});

  @override
  Widget build(BuildContext){
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              const GFAvatar(
                size: 80,
                child: Icon(Icons.person, size: 60, color: Colors.white),
                backgroundColor: Colors.blueGrey,
              ),
              const SizedBox(height: 16),
              const Text(
                'Захар',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              ),
              const Text(
                'Символ красоты',
                style: TextStyle(fontSize: 16, color: Colors.cyan),
              ),
              const SizedBox(height: 24),
              GFRating(
                value: 5, 
                itemCount: 5, 
                size: GFSize.SMALL,
                color: Colors.amber,
                borderColor: Colors.amber,
                allowHalfRating: true,
                onChanged: (value) {},
              ),
              const SizedBox(height: 24),
              GFListTile(
                titleText: 'Email',
                subTitleText: 'zaharik_luchshiy@gmail.com',
                icon: const Icon(Icons.email),
              ),
              GFListTile(
                titleText: 'Phone',
                subTitleText: '89246274877',
                icon: const Icon(Icons.phone),
              ),
            ],
          ),
        ),
      ),
    );
  }
}