"""Punto de entrada de la aplicación Flet."""

import flet as ft

from services.calculator_service import CalculatorService
from ui.layout import CalculatorLayout
from ui.theme import COLOR_BG


class CalculatorApp:
    """Aplicación principal de la calculadora."""

    def __init__(self, page: ft.Page) -> None:
        self._page = page
        self._service = CalculatorService()
        self._equation = ""
        self._result = "0"
        self._setup_page()
        self._create_ui()

    def _setup_page(self) -> None:
        self._page.title = "Calculadora"
        self._page.theme_mode = ft.ThemeMode.DARK
        self._page.bgcolor = COLOR_BG
        self._page.padding = 0
        # Eliminamos propiedades window_* conflictivas. 
        # Hyprland se encargará del tamaño mediante windowrulev2.

    def _create_ui(self) -> None:
        self._layout = CalculatorLayout(on_button_click=self._handle_button)
        self._page.add(self._layout)

    def _handle_button(self, button: str) -> None:
        if button == "C":
            self._clear()
        elif button == "⌫":
            self._backspace()
        elif button == "=":
            self._calculate()
        elif button == "%":
            self._percentage()
        elif button in ["+", "−", "×", "÷"]:
            self._add_operator(button)
        else:
            self._add_digit(button)

        self._update_display()

    def _add_digit(self, digit: str) -> None:
        if digit == "." and "." in self._equation.split()[-1]:
            return
        self._equation += digit

    def _add_operator(self, operator: str) -> None:
        if not self._equation:
            return
        last_char = self._equation[-1] if self._equation else ""
        if last_char in ["+", "−", "×", "÷"]:
            self._equation = self._equation[:-1] + operator
        else:
            self._equation += f" {operator} "

    def _backspace(self) -> None:
        if self._equation:
            if self._equation[-1] == " ":
                self._equation = self._equation[:-3]
            else:
                self._equation = self._equation[:-1]

    def _clear(self) -> None:
        self._equation = ""
        self._result = "0"

    def _calculate(self) -> None:
        if not self._equation:
            return
        try:
            parts = self._equation.split()
            if len(parts) < 3:
                return

            result = 0.0
            i = 0
            while i < len(parts):
                if i == 0:
                    result = float(parts[i])
                    i += 1
                    continue

                op = parts[i]
                num = float(parts[i + 1])

                if op == "+":
                    result = self._service.perform_addition(result, num).result
                elif op == "−":
                    result = self._service.perform_subtraction(result, num).result
                elif op == "×":
                    result = self._service.perform_multiplication(result, num).result
                elif op == "÷":
                    result = self._service.perform_division(result, num).result

                i += 2

            self._result = self._format_result(result)
        except Exception as e:
            self._result = str(e)
            self._layout.display.show_error(self._result)

    def _percentage(self) -> None:
        if not self._equation:
            return
        try:
            parts = self._equation.split()
            if len(parts) >= 2:
                value = float(parts[-1])
                calc = self._service.perform_percentage(value, 100)
                self._equation = " ".join(parts[:-1]) + " " + str(calc.result)
                self._result = self._format_result(calc.result)
        except Exception as e:
            self._layout.display.show_error(str(e))

    def _format_result(self, value: float) -> str:
        if value == int(value):
            return str(int(value))
        return str(value)

    def _update_display(self) -> None:
        self._layout.display.update_display(self._equation, self._result)


def main(page: ft.Page) -> None:
    CalculatorApp(page)


if __name__ == "__main__":
    ft.run(main)
