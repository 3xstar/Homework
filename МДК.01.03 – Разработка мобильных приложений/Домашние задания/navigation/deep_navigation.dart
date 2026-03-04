import 'package:flutter/material.dart';
import 'package:getwidget/getwidget.dart';

class BottomNav extends StatefulWidget {
  const BottomNav({super.key});

  @override
  State<BottomNav> createState() => _BottomNavState();
}

class HomePage extends StatelessWidget {
  HomePage({super.key});

  final List<String> items = List.generate(30, (index) => 'Пользователь $index');

  @override
  Widget build(BuildContext context){
    return ListView(
          children: ListTile.divideTiles(
            context: context,
            tiles: items.map((item) => ListTile(
              leading: CircleAvatar(
                backgroundImage: AssetImage('good_person.jpg'),
              ),
              title: Text(item),
              subtitle: Text("Какое-то там описание"),
          ))
        ).toList(),
      );
  }
}

final TextEditingController _searchController = TextEditingController();

class SearchPage extends StatelessWidget {
  
  SearchPage({super.key});

  @override
  Widget build(BuildContext context){
    return Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                children: [
                  TextField
                  (
                    controller: _searchController,
                    decoration: InputDecoration(
                      labelText: 'Введите имя',
                      border: const OutlineInputBorder(),
                      ),
                  ),
                  const SizedBox(height: 20),
                  ElevatedButton(onPressed: (){
                    showDialog(context: context,
                    builder: (BuildContext context) {
                      return AlertDialog(
                        title: Text("Подтверждение"),
                        content: Text("Искать ${_searchController.text}?"),
                        actions: [
                          TextButton(
                            onPressed: () => Navigator.pop(context),
                            child: Text('Нет')),
                          TextButton(
                            onPressed: () => Navigator.pop(context),
                            child: Text('Да')),
                        ],
                      );
                    },
                    );
                  }, child: Text('Найти'))
                ],
              ),
            );
          }
        }


class _BottomNavState extends State<BottomNav> {
  int _selectedIndex = 0;

  static List<Widget> screenList = <Widget>[
    HomePage(),
    SearchPage(),
    Center(
      child: Text('Профиль')
    )
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text('Навигация'),
        ),

        body: screenList.elementAt(_selectedIndex),
        // Захар
        bottomNavigationBar: BottomNavigationBar(
          items: [
            BottomNavigationBarItem(
              icon: Icon(Icons.home),
              label: 'Главная'
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.search),
              label: 'Поиск'
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.person),
              label: 'Профиль'
            ),
          ],
          currentIndex: _selectedIndex,
          selectedItemColor: Colors.amber,
          onTap: _onItemTapped
        ),
      ),
    );
  }
}