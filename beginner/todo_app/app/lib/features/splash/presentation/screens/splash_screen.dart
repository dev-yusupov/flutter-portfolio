import 'package:flutter/material.dart';

class SplashScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    _navigateToNextPage(context);
    return const Scaffold(
        body: Center(
      child: Column(
        children: [
          Text("Todo App"),
        ],
      ),
    ));
  }

  void _navigateToNextPage(BuildContext context) async {}
}
