import 'package:flutter/material.dart';
import 'package:getwidget/getwidget.dart';

class BasicApp extends StatelessWidget {
  const BasicApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Редактирование пользователя',
      home: ProfileScreen(),
    );
  }
}

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class UserData{
String name = "Саша";
String status = "Посещает пары";
}

class _ProfileScreenState extends State<ProfileScreen> {
  final UserData userData = UserData();

  void _changeScreen() async {
    final result = await Navigator.push(
      context, 
      MaterialPageRoute(
        builder: (context) => EditProfileScreen(
        currentName: userData.name,
        currentStatus: userData.status
        ),
      ),
    );

    if(result != null && result is Map<String, String>) {
      setState(() {
        userData.name = result['name'] ?? userData.name;
        userData.status = result['status'] ?? userData.name;
      });
    }
  }


  @override
  Widget build(BuildContext content) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blueAccent,
        title: Text('Профиль пользователя'),
      ),
      body: Center(
        child: Column(
          children: [
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                GFCard(
                  title:GFListTile(
                    avatar: const GFAvatar(
                      child: Icon(Icons.person),
                    ),
                  title: const Text(
                    'Пользователь',
                    style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20),
                  ),
                ),                  
                content: Padding(
                  padding: const EdgeInsets.all(10),
                  child: Column(
                  children: [
                    Text(
                      "Имя: ${userData.name}\nСтатус: ${userData.status}",
                      style: TextStyle(fontSize: 25),
                    ), 
                    const SizedBox(height: 30),
                    GFButton(
                      padding: EdgeInsets.symmetric(horizontal: 50),
                      text: 'Редактировать', textStyle: TextStyle(fontSize: 25, color: Colors.white),
                      onPressed: () => _changeScreen(),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ],
    ),
  ),
);
}
}


class EditProfileScreen extends StatefulWidget {
  final String currentName;
  final String currentStatus;

  const EditProfileScreen({
    super.key,
    required this.currentName,
    required this.currentStatus});

  @override
  State<EditProfileScreen> createState() => _EditProfileScreenState();
}

class _EditProfileScreenState extends State<EditProfileScreen> {
  late TextEditingController nameController;
  late TextEditingController statusController;

  @override
  void initState(){
    super.initState();
    nameController = TextEditingController(text: widget.currentName);
    statusController = TextEditingController(text: widget.currentStatus);
  }

  @override
  void dispose() {
    nameController.dispose();
    statusController.dispose();
    super.dispose();
  }

  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Редактирование'),
      ),
      body: Center(
        child: Column(
          children: [
            SizedBox(height: 30),
            TextField(
              controller: nameController,
              decoration: InputDecoration(
                labelText: "Имя пользователя",
                border: const OutlineInputBorder(),
            ),
            ),
            const SizedBox(height: 30),
            TextField(
              controller: statusController,
              decoration: InputDecoration(
                labelText: "Статус",
                border: const OutlineInputBorder(),
            ),
            ),
            const SizedBox(height: 30),
            GFButton(
              color: Colors.green,
              padding: EdgeInsets.symmetric(horizontal: 50),
              text: 'Сохранить', textStyle: TextStyle(fontSize: 25, color: Colors.white),
              onPressed: () {
              Navigator.pop(context, {
              'name': nameController.text,
              'status': statusController.text,
              });
            },
          ),
        ],
      ),
    ),
);
}
}