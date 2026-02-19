import 'package:flutter/material.dart';
import 'package:getwidget/getwidget.dart';


class RegisterForm extends StatefulWidget {
  const RegisterForm ({super.key});

  @override
  State<RegisterForm> createState() => _RegisterFormState();
}

class _RegisterFormState extends State<RegisterForm> {
  late TextEditingController _usernameController;
  late TextEditingController _passwordController;

  String? _errorText = '';
  String? _errorText2 = '';

  @override
  void initState(){
    super.initState();
    _usernameController = TextEditingController();
    _passwordController = TextEditingController();
  }


  @override
  void dispose() {
    _usernameController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  void _validationName(String username){
    setState(() {
      if (username.length < 3){
        _errorText = 'введите имя длиннее двух символов';
      }
      else if (username.contains(' ')) {
        _errorText = 'в имени не должно быть пробелов';
      }
      else if (username.contains('захар123')) {
        _errorText = 'одумайся';
      }
      else{
        _errorText = null;
      }
    });
  }

  void _validationPassword(String password){
    setState(() {
    if (password.length < 8){
      _errorText2 = 'Пароль слишком короткий (минимум 8 символов)';
    } else if (!password.contains(RegExp(r'[A-Z]'))) {
      _errorText2 = 'Добавьте хотя бы одну заглавную букву';
    } else if (!password.contains(RegExp(r'[0-9]'))) {
      _errorText2 = 'Добавьте хотя бы одну цифру';
    } else if (!password.contains(RegExp(r'[!@#$%^&*(),.?":{}|<>]'))) {
      _errorText2 = 'Добавьте хотя бы один специальный символ';
    }
    else{
        _errorText2 = null;
      }
    });
  }

  void _register(BuildContext context){
    final username = _usernameController.text;
    _validationName(username);
    final password = _passwordController.text;
    _validationPassword(password);

    if (_errorText == null && _errorText2 == null) {
      GFToast.showToast('Пользователь с именем "$username зарегистрирован',
      context,
      backgroundColor: GFColors.SUCCESS,
      toastPosition: GFToastPosition.BOTTOM
      );
    }
    else {
      GFToast.showToast(
        _errorText!,
        context,
        backgroundColor: GFColors.DANGER,
        toastPosition: GFToastPosition.BOTTOM,
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.indigoAccent,
        body: Builder(
          builder: (BuildContext innerContext) {
            return Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                children: [
                  GFCard(
                    color: Colors.white,
                    content: Column(
                      children: [
                        TextField(
                          controller: _usernameController,
                          onChanged: _validationName,
                          onSubmitted: (_) => _register(innerContext),
                          decoration: InputDecoration(
                            labelText: 'Введите имя',
                            errorText: _errorText,
                            border: const OutlineInputBorder(),
                          ),
                        ),
                        const SizedBox(height: 20),
                        TextField(
                          controller: _passwordController,
                          onChanged: _validationPassword,
                          onSubmitted: (_) => _register(innerContext),
                          decoration: InputDecoration(
                            labelText: 'Введите пароль',
                            errorText: _errorText2,
                            border: const OutlineInputBorder(),
                          ),
                        ),
                        const SizedBox(height: 10),
                        GFButton(
                          color: Colors.cyan,
                          onPressed: () => _register(innerContext),
                          text: "Зарегистрироваться",
                          blockButton: true,
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            );
          }
        )
      )
    );
  }
}