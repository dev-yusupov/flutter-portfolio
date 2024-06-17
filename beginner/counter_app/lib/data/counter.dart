// Counter model

class Counter {
  int value; // Set counter model data

  Counter({required this.value});

  int getValue() => value; // Returns the value

  void incrementValue() {
    value++; // Increases the current value by 1
  }

  void decrementValue() {
    value--; // Decreases the current value by 1
  }

  void resetvalue() {
    value = 0;
  }
}
