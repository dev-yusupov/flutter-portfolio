import 'package:flutter/material.dart';

class LightColorSchema {
  static const Color primaryColor1 = Color(0xFFF0F0F0); // Light Background
  static const Color primaryColor2 = Color(0xFF333333); // Dark Text
  static const Color primaryColor3 = Color(0xFF218BFF); // Blue Accent

  // Status colors
  static const Color statusSuccess = Color(0xFF4CAF50);
  static const Color statusError = Color(0xFFDC3545);
  static const Color statusWarning = Color(0xFFFFC107);
  static const Color statusInfo = Color(0xFF17A2B8);

  // Additional Colors
  static const Color secondaryColor = Color(0xFF757575);
  static const Color surfaceColor = Color(0xFFFFFFFF);
  static const Color backgroundColor =
      Color(0xFFEFEFEF);
}

ColorScheme lightColorScheme = const ColorScheme(
  brightness: Brightness.light,
  primary: LightColorSchema.primaryColor3,
  onPrimary: LightColorSchema.primaryColor1,
  secondary: LightColorSchema.secondaryColor,
  onSecondary: LightColorSchema.primaryColor1,
  error: LightColorSchema.statusError,
  onError: LightColorSchema.primaryColor1,
  surface: LightColorSchema.surfaceColor,
  onSurface: LightColorSchema.primaryColor2,
);


class DarkColorSchema {
  static const Color primaryColor1 = Color(0xFF3A3A3C); // Light Background
  static const Color primaryColor2 = Color(0xFFE5E5EA); // Dark Text
  static const Color primaryColor3 = Color(0xFF00D1D1); // Blue Accent

  // Status colors
  static const Color statusSuccess = Color(0xFF4CAF50);
  static const Color statusError = Color(0xFFDC3545);
  static const Color statusWarning = Color(0xFFFFC107);
  static const Color statusInfo = Color(0xFF17A2B8);

  // Additional Colors
  static const Color secondaryColor = Color(0xFF757575);
  static const Color surfaceColor = Color(0xFFFFFFFF);
  static const Color backgroundColor =
      Color(0xFFEFEFEF);
}

ColorScheme darkColorScheme = const ColorScheme(
  brightness: Brightness.light,
  primary: DarkColorSchema.primaryColor3,
  onPrimary: DarkColorSchema.primaryColor1,
  secondary: DarkColorSchema.secondaryColor,
  onSecondary: DarkColorSchema.primaryColor1,
  error: DarkColorSchema.statusError,
  onError: DarkColorSchema.primaryColor1,
  surface: DarkColorSchema.surfaceColor,
  onSurface: DarkColorSchema.primaryColor2,
);