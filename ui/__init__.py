"""Módulo de interfaz de usuario para la calculadora."""

from ui.app import main
from ui.layout import CalculatorLayout
from ui.panels.display import DisplayPanel
from ui.panels.keypad import KeypadPanel
from ui.theme import (
    BTN_ACTION,
    BTN_CLEAR,
    BTN_DEFAULT,
    BTN_EQUAL,
    BTN_OPERATOR,
    COLOR_BG,
    COLOR_BUTTON,
    COLOR_BTN_TEXT,
    COLOR_CLEAR,
    COLOR_EQUATION,
    COLOR_EQUAL_BG,
    COLOR_RESULT,
)

__all__ = [
    "main",
    "CalculatorLayout",
    "DisplayPanel",
    "KeypadPanel",
    "BTN_ACTION",
    "BTN_CLEAR",
    "BTN_DEFAULT",
    "BTN_EQUAL",
    "BTN_OPERATOR",
    "COLOR_BG",
    "COLOR_BUTTON",
    "COLOR_BTN_TEXT",
    "COLOR_CLEAR",
    "COLOR_EQUATION",
    "COLOR_EQUAL_BG",
    "COLOR_RESULT",
]
