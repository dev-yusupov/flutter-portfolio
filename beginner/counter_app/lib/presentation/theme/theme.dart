import 'package:flutter/material.dart';

class AppColors {
  static const Color primaryColor = Colors.blue;
  static const Color accentColor = Colors.teal;
  static const Color backgroundColor = Colors.white;
  static const Color textColor = Colors.black;
  static const Color buttonColor = Colors.blueAccent;
}

class AppDarkColors {
  static const Color primaryColor = Color.fromARGB(255, 0, 30, 54);
  static const Color accentColor = Color(0xFF3EFFEC); // Light teal
  static const Color backgroundColor =
      Color.fromARGB(255, 7, 77, 134); // Dark grey
  static const Color textColor = Colors.white;
  static const Color buttonColor = Color(0xFF1C6FFF); // Dark blue
}

class AppTypography {
  static const TextStyle headingStyle = TextStyle(
    fontSize: 24,
    fontWeight: FontWeight.bold,
    color: AppColors.textColor,
  );

  static const TextStyle buttonTextStyle = TextStyle(
    fontSize: 18.0,
    fontWeight: FontWeight.bold,
    color: Colors.white,
  );

  static const TextStyle counterTextStyle = TextStyle(
    fontSize: 48.0,
    fontWeight: FontWeight.bold,
    color: AppColors.primaryColor,
  );
}

class AppTheme {
  static ThemeData lightTheme = ThemeData(
    primaryColor: AppColors.primaryColor,
    scaffoldBackgroundColor: AppColors.backgroundColor,
    colorScheme: const ColorScheme.light(
      primary: AppColors.primaryColor,
      secondary: AppColors.accentColor,
      surface: AppColors.primaryColor,
      onPrimary: Colors.white,
      onSecondary: Colors.white,
      onError: Colors.white,
      onSurface: AppColors.accentColor,
    ),
    buttonTheme: ButtonThemeData(
      buttonColor: AppColors.buttonColor,
      textTheme: ButtonTextTheme.primary,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(8.0),
      ),
    ),
    appBarTheme: const AppBarTheme(
      backgroundColor: AppColors.primaryColor,
      titleTextStyle: TextStyle(color: Colors.white, fontSize: 24.0),
    ),
  );

  static ThemeData darkTheme = ThemeData(
    primaryColor: AppDarkColors.primaryColor,
    scaffoldBackgroundColor: AppDarkColors.backgroundColor,
    colorScheme: const ColorScheme.dark(
      primary: AppDarkColors.primaryColor,
      secondary: AppDarkColors.accentColor,
      surface: AppDarkColors.primaryColor,
      onPrimary: Colors.white,
      onSecondary: Colors.white,
      onError: Colors.white,
      onSurface: AppDarkColors.accentColor,
    ),
    buttonTheme: ButtonThemeData(
      buttonColor: AppDarkColors.buttonColor,
      textTheme: ButtonTextTheme.primary,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(8.0),
      ),
    ),
    appBarTheme: const AppBarTheme(
      backgroundColor: AppDarkColors.primaryColor,
      titleTextStyle: TextStyle(color: Colors.white, fontSize: 24.0),
    ),
  );
}
