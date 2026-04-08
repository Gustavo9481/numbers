"""Panel de teclado numérico de la calculadora."""

import flet as ft

from ui.theme import (
    BTN_ACTION,
    BTN_CLEAR,
    BTN_DEFAULT,
    BTN_EQUAL,
    BTN_OPERATOR,
    BUTTON_BORDER_RADIUS,
    BUTTON_HEIGHT,
    FONT_SIZE_BUTTON,
    KEYPAD_GAP,
)


class KeypadPanel(ft.Container):
    """Panel que contiene el teclado numérico de la calculadora."""

    def __init__(self, on_button_click: callable) -> None:
        self._on_button_click = on_button_click
        super().__init__(
            padding=8,
            expand=True,
        )
        self._build_keypad()

    def _build_keypad(self) -> None:
        buttons = [
            self._create_row(
                ["C", "%", "⌫", "÷"], [BTN_CLEAR, BTN_ACTION, BTN_ACTION, BTN_OPERATOR]
            ),
            self._create_row(
                ["7", "8", "9", "×"], [BTN_DEFAULT, BTN_DEFAULT, BTN_DEFAULT, BTN_OPERATOR]
            ),
            self._create_row(
                ["4", "5", "6", "−"], [BTN_DEFAULT, BTN_DEFAULT, BTN_DEFAULT, BTN_OPERATOR]
            ),
            self._create_row(
                ["1", "2", "3", "+"], [BTN_DEFAULT, BTN_DEFAULT, BTN_DEFAULT, BTN_OPERATOR]
            ),
            self._create_row(["", "0", ".", "="], [None, BTN_DEFAULT, BTN_DEFAULT, BTN_EQUAL]),
        ]

        self.content = ft.Column(
            controls=buttons,
            spacing=KEYPAD_GAP,
            alignment=ft.MainAxisAlignment.END,
        )

    def _create_row(self, labels: list, styles: list) -> ft.Row:
        buttons = []
        for label, style in zip(labels, styles):
            if label == "":
                buttons.append(ft.Container(width=64))
            else:
                buttons.append(self._create_button(label, style))
        return ft.Row(controls=buttons, spacing=KEYPAD_GAP)

    def _create_button(self, label: str, style: dict) -> ft.Container:
        if label == "=":
            is_equal = True
        else:
            is_equal = False

        btn = ft.Container(
            content=ft.Text(
                value=label,
                size=FONT_SIZE_BUTTON,
                color=style["color"],
                text_align=ft.TextAlign.CENTER,
            ),
            bgcolor=style["bgcolor"],
            width=64,
            height=BUTTON_HEIGHT,
            border_radius=BUTTON_BORDER_RADIUS,
            on_click=self._handle_click,
            data=label,
            ink=True,
        )

        if is_equal:
            btn.expand = 1

        return btn

    def _handle_click(self, e: ft.ControlEvent) -> None:
        button_label = e.control.data
        if button_label and self._on_button_click:
            self._on_button_click(button_label)
