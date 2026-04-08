"""Panel de visualización de la calculadora."""

import flet as ft

from ui.theme import (
    COLOR_BG,
    COLOR_EQUATION,
    COLOR_RESULT,
    FONT_SIZE_EQUATION,
    FONT_SIZE_RESULT,
)


class DisplayPanel(ft.Container):
    """Panel que muestra la ecuación en curso y el resultado."""

    def __init__(self) -> None:
        self._equation = "0"
        self._result = "0"
        super().__init__(
            bgcolor=COLOR_BG,
            padding=20,
            expand=True,
        )
        self._build_content()

    def _build_content(self) -> None:
        self.content = ft.Column(
            controls=[
                self._equation_text,
                self._result_text,
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=8,
        )

    @property
    def _equation_text(self) -> ft.Text:
        return ft.Text(
            value=self._equation,
            size=FONT_SIZE_EQUATION,
            color=COLOR_EQUATION,
            text_align=ft.TextAlign.RIGHT,
            overflow=ft.TextOverflow.VISIBLE,
        )

    @property
    def _result_text(self) -> ft.Text:
        return ft.Text(
            value=self._result,
            size=FONT_SIZE_RESULT,
            color=COLOR_RESULT,
            text_align=ft.TextAlign.RIGHT,
            overflow=ft.TextOverflow.VISIBLE,
        )

    def update_display(self, equation: str, result: str) -> None:
        """Actualiza los valores mostrados en el display."""
        self._equation = equation if equation else "0"
        self._result = result if result else "0"
        self.content = ft.Column(
            controls=[
                ft.Text(
                    value=self._equation,
                    size=FONT_SIZE_EQUATION,
                    color=COLOR_EQUATION,
                    text_align=ft.TextAlign.RIGHT,
                    overflow=ft.TextOverflow.VISIBLE,
                ),
                ft.Text(
                    value=self._result,
                    size=FONT_SIZE_RESULT,
                    color=COLOR_RESULT,
                    text_align=ft.TextAlign.RIGHT,
                    overflow=ft.TextOverflow.VISIBLE,
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=8,
        )
        self.update()

    def show_error(self, message: str) -> None:
        """Muestra un mensaje de error en el panel de resultado."""
        self._result = message
        self.content = ft.Column(
            controls=[
                ft.Text(
                    value=self._equation,
                    size=FONT_SIZE_EQUATION,
                    color=COLOR_EQUATION,
                    text_align=ft.TextAlign.RIGHT,
                    overflow=ft.TextOverflow.VISIBLE,
                ),
                ft.Text(
                    value=self._result,
                    size=FONT_SIZE_RESULT,
                    color="#e63946",
                    text_align=ft.TextAlign.RIGHT,
                    overflow=ft.TextOverflow.VISIBLE,
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=8,
        )
        self.update()

    def clear(self) -> None:
        """Limpia el display."""
        self.update("0", "0")
