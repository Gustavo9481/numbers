## Why

El proyecto PyCalc necesita un archivo .gitignore adecuado para mantener limpio el repositorio, evitando que archivos temporales, de configuración local, y artefactos de build se suban al repositorio remoto público.

## What Changes

- Crear archivo .gitignore en la raíz del proyecto
- Ignorar carpetas de metadata: .gemini, .opencode, .openspec
- Ignorar archivos de configuración local: AGENTS.md, proposal.md
- Ignorar entornos virtuales y caches: .venv, __pycache__, .pytest_cache
- Ignorar archivos de build Rust: target/, *.pyd, *.so
- Ignorar archivos de IDE y OS: .vscode/, .idea/, *.swp, .DS_Store

## Capabilities

### New Capabilities

- `gitignore-config`: Archivo de configuración gitignore con todas las reglas necesarias para el proyecto

## Impact

- Nuevo archivo `.gitignore` en la raíz del proyecto
- Afecta el flujo de git (qué archivos se tracking)
