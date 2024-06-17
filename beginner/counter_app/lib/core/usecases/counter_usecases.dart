import 'package:counter_app/presentation/counter_provider.dart';

class IncrementCounterUseCase {
  final CounterProvider counterProvider;

  IncrementCounterUseCase({required this.counterProvider});

  void execute() {
    counterProvider.increment();
  }
}

class DecrementCounterUseCase {
  final CounterProvider counterProvider;

  DecrementCounterUseCase({required this.counterProvider});

  void execute() {
    counterProvider.decrement();
  }
}

class ResetCounterUseCase {
  final CounterProvider counterProvider;

  ResetCounterUseCase({required this.counterProvider});

  void execute() {
    counterProvider.reset();
  }
}
