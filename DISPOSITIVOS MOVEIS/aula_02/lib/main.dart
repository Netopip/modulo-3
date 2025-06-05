import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const MyHomePage(),
    );
  }
}


class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('My App'),
      backgroundColor: Colors.blue,),
      
      drawer: Drawer(child: ListView(
      padding: EdgeInsets.zero,
      children: [
        DrawerHeader(
          decoration: BoxDecoration(
            color: Colors.blue,
          ),
          child: Text('Menu', style: TextStyle(color: Colors.white, fontSize: 24)),
        ),
        ListTile(
          leading: Icon(Icons.home),
          title: Text('Início'),
          onTap: () {
            // Ação ao clicar no item
            Navigator.pop(context);
          },
        ),
        ListTile(
          leading: Icon(Icons.map),
          title: Text('Mapa'),
          onTap: () {
            // Ação ao clicar no item
            Navigator.pop(context);
          },
        ),
      ],
    ),
    ),
    
      body: Center(child: Text('texto'),),
      backgroundColor: const Color.fromARGB(255, 205, 209, 210),
      bottomNavigationBar: BottomNavigationBar(items: 
      [
      BottomNavigationBarItem(icon: Icon(Icons.settings),label: 'Configurações'),
      BottomNavigationBarItem(icon: Icon(Icons.person),label: 'Usuários'),
      //BottomNavigationBarItem(icon: Icon(Icons.access_time),label: 'Horas'),
      BottomNavigationBarItem(icon: Icon(Icons.access_alarm),label: 'Alarme'),
      ],
      backgroundColor: const Color.fromARGB(255, 255, 213, 4), 
      ),
    );
  }
}

