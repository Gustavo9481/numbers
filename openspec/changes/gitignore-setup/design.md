## Context

El proyecto PyCalc está en desarrollo inicial. Actualmente no existe un archivo .gitignore, lo que significa que archivos temporales, entornos virtuales, y artefactos de compilación podrían subirse accidentalmente al repositorio público.

## Goals / Non-Goals

**Goals:**
- Crear .gitignore completo que cubra todas las carpetas y archivos temporales del proyecto
- Mantener el repositorio limpio de archivos de configuración local

**Non-Goals:**
- Configurar git remote o integración con servicios externos
- Ignorar archivos de código fuente que deben estar en el repositorio

## Decisions

1. **Estructura del gitignore**: Usar template Python .gitignore como base
   - Razón: Proyectos Python tienen patrones comunes bien establecidos
   - Alternativa: Crear desde cero - más trabajo y propenso a errores

2. **Carpetas de metadata**: Ignorar .gemini, .opencode, .openspec
   - Razón: El usuario específicamente las solicitó
   - Estas carpetas contienen configuración de herramientas de IA

## Risks / Trade-offs

- [Risk] Olvidar alguna carpeta temporal → [Mitigation] Revisar estructura actual del proyecto
- [Risk] Ignorar archivos necesarios → [Mitigation] Mantener solo archivos de configuración en ignore
