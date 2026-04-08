## Context
Ajuste de la UI para que sea flotante y centrada en Hyprland/Wayland.

## Decisions
- Utilizar `page.window_always_on_top = True` (opcional) y `page.window_resizable = False` en Flet.
- Asegurar que el título de la ventana sea único para facilitar las reglas del WM.
- Proponer una regla de Hyprland basada en la clase y el título.

## Implementation Details
### Flet (ui/app.py)
Añadir las siguientes propiedades en `_setup_page`:
```python
self._page.window_width = 340
self._page.window_height = 580
self._page.window_resizable = False
self._page.window_movable = True
self._page.window_focused = True
# Propiedad para ayudar a los WMs a identificarla como utilidad
self._page.window_prevent_close = False
```

### Hyprland Rule
La regla recomendada para `~/.config/hypr/hyprland.conf` es:
```bash
windowrulev2 = float, class:(flet), title:(Calculadora)
windowrulev2 = size 340 580, class:(flet), title:(Calculadora)
windowrulev2 = center, class:(flet), title:(Calculadora)
```
