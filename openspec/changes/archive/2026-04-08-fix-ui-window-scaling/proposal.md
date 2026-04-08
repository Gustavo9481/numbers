## Why

La calculadora se abre en pantalla completa (modo mosaico) en Hyprland, lo que distorsiona su diseño pensado para una ventana de 340x580. Dado que Hyprland es un gestor de ventanas tipo tiling, es necesario forzar el modo flotante para mantener la usabilidad y estética de la aplicación.

## What Changes

- Modificación de las propiedades de la ventana en `ui/app.py` para solicitar modo flotante.
- Inclusión de una recomendación de configuración para Hyprland (windowrule) para asegurar el comportamiento deseado.

## Capabilities

### New Capabilities
- `window-management`: Gestión de las propiedades de la ventana de la aplicación para entornos de escritorio modernos (Wayland/X11).

### Modified Capabilities
- Ninguna (no hay cambios en la lógica aritmética).

## Impact

- `ui/app.py`: Ajuste de configuración de Flet.
- Entorno de usuario: Requiere añadir una regla en la configuración de Hyprland.
