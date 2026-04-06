## ADDED Requirements

### Requirement: Generación de reporte de cobertura
El sistema SHALL permitir la generación de reportes de cobertura para las pruebas de Python utilizando `pytest-cov`.

#### Scenario: Reporte en terminal
- **WHEN** se ejecuta `pytest --cov`
- **THEN** la terminal muestra un resumen porcentual de las líneas cubiertas por archivo

#### Scenario: Reporte HTML
- **WHEN** se ejecuta la generación de cobertura con el formato `html`
- **THEN** se crea un directorio `htmlcov/` con el detalle visual de la cobertura

### Requirement: Configuración en pyproject.toml
La configuración de cobertura MUST estar centralizada en `pyproject.toml` para evitar el uso de archivos de configuración externos adicionales.

#### Scenario: Persistencia de configuración
- **WHEN** el archivo `pyproject.toml` contiene la sección `[tool.coverage.run]`
- **THEN** al ejecutar `pytest` se aplican automáticamente los parámetros de cobertura configurados
