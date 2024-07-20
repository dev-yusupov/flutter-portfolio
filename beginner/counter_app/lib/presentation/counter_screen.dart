import 'package:counter_app/core/usecases/counter_usecases.dart';
import 'package:counter_app/presentation/counter_provider.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class CounterScreen extends StatelessWidget {
  const CounterScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final counter = Provider.of<CounterProvider>(context);
    final increment = IncrementCounterUseCase(counterProvider: counter);
    final decrement = DecrementCounterUseCase(counterProvider: counter);
    final reset = ResetCounterUseCase(counterProvider: counter);

    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Container(
            width: MediaQuery.of(context).size.width / 2,
            height: MediaQuery.of(context).size.width / 2,
            alignment: Alignment.center,
            decoration: BoxDecoration(
              color: Theme.of(context).colorScheme.primary,
              borderRadius: BorderRadius.circular(30),
            ),
            child: Text(
              counter.value.toString(),
              style: const TextStyle(
                color: Colors.white,
                fontWeight: FontWeight.bold,
                fontSize: 86,
              ),
            ),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              ElevatedButton(
                  onPressed: reset.execute,
                  child: Icon(
                    Icons.restore,
                    size: 23,
                    color: Theme.of(context).colorScheme.onSecondary,
                  )),
              ElevatedButton(
                onPressed: increment.execute,
                child: Text(
                  "+",
                  style: TextStyle(
                      color: Theme.of(context).colorScheme.onSecondary,
                      fontSize: 26),
                ),
              ),
              ElevatedButton(
                onPressed: decrement.execute,
                child: Text(
                  "-",
                  style: TextStyle(
                      color: Theme.of(context).colorScheme.onSecondary,
                      fontSize: 26),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
