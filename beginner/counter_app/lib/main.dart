import 'package:counter_app/data/counter.dart';
import 'package:counter_app/presentation/counter_provider.dart';
import 'package:counter_app/presentation/counter_screen.dart';
import 'package:counter_app/presentation/theme/theme.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();

  SystemChrome.setEnabledSystemUIMode(SystemUiMode.immersive);

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      themeMode: ThemeMode.system,
      home: ChangeNotifierProvider(
        create: (context) => CounterProvider(counter: Counter(value: 0)),
        child: CounterScreen(),
      ),
    );
  }
}
