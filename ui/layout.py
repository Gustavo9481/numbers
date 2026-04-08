"""Composición general de la ventana y paneles."""

import flet as ft

from ui.panels.display import DisplayPanel
from ui.panels.keypad import KeypadPanel
from ui.theme import COLOR_BG


class CalculatorLayout(ft.Container):
    """Layout principal que contiene todos los paneles de la calculadora."""

    def __init__(self, on_button_click: callable) -> None:
        self._on_button_click = on_button_click
        self._display = DisplayPanel()
        self._keypad = KeypadPanel(on_button_click)

        super().__init__(
            bgcolor=COLOR_BG,
            padding=10,
            width=320,
        )
        self._build_layout()

    def _build_layout(self) -> None:
        self.content = ft.Column(
            controls=[
                self._display,
                ft.Container(height=10),
                self._keypad,
            ],
            spacing=0,
            alignment=ft.MainAxisAlignment.START,
        )

    @property
    def display(self) -> DisplayPanel:
        return self._display

    @property
    def keypad(self) -> KeypadPanel:
        return self._keypad
