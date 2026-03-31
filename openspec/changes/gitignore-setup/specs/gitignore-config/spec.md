## ADDED Requirements

### Requirement: Archivo .gitignore completo
El proyecto SHALL tener un archivo .gitignore en la raíz que ignore todos los archivos y carpetas temporales, de configuración local, y artefactos de build.

#### Scenario: Python project ignore patterns
- **WHEN** se crea el archivo .gitignore con template Python estándar
- **THEN** ignora entornos virtuales, caches Python, y archivos de pytest

#### Scenario: Metadata folders ignore
- **WHEN** se agregan reglas para .gemini, .opencode, .openspec
- **THEN** estas carpetas de metadata de IA no se suben al repositorio

#### Scenario: Rust build artifacts ignore
- **WHEN** se agregan reglas para target/ y archivos .so/.pyd
- **THEN** los artefactos de compilación Rust no se tracking

#### Scenario: IDE and OS files ignore
- **WHEN** se agregan reglas para .vscode/, .idea/, .DS_Store
- **THEN** archivos del IDE y SO no se suben al repositorio

#### Scenario: Config files ignore
- **WHEN** se agregan reglas para AGENTS.md y proposal.md
- **THEN** archivos de configuración local no se suben al repositorio
