import 'package:shared_preferences/shared_preferences.dart';

class CounterRepository {
  static const counterKey = "counter";

  Future<int> getCounter() async {
    final prefs = await SharedPreferences.getInstance();
    final value = prefs.getInt(counterKey) ??
        0; // Gets value from shared preferences. If it is null then it will take 0 automatically

    return value; // returns the value
  }

  Future<void> saveCounter(int value) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setInt(counterKey, value);
  }
}
