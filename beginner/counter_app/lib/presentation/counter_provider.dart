import 'package:counter_app/data/counter.dart';
import 'package:flutter/material.dart';

class CounterProvider extends ChangeNotifier {
  final Counter counter;

  CounterProvider({required this.counter});

  int get value => counter.value;

  void increment() {
    counter.incrementValue();
    notifyListeners();
  }

  void decrement() {
    counter.decrementValue();
    notifyListeners();
  }

  void reset() {
    counter.resetvalue();
    notifyListeners();
  }
}
