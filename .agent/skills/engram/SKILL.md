---
name: engram 
description: Skill para el guardado de notas en memoria persistente en la app engram cuando el usuario solicite un backup en engram. 
---

Esta skill permite guardar notas en memoria persistente en la app engram. Las notas tendran una redacción útil para que gemini pueda procesarlas correctamente.La idea es que el agente tenga un contexto claro de las tareas que realizó o el estado del proyecto.

## TRIGGER
El lanzador para ésta skill será cuando el usuario solicite un backup en engram o anuncie el cierre de la sesión.

## FORMATO DE NOTAS
- Usar una etiqueta con el nombre del proyecto, mantenerla si se hacen varias notas del mismo. 
  -Ejemplo: 'proyecto-tareas'.
- Usar estas guías para estructurar las notas, incluyendo las palabras clave:
  - STATUS: características,estado actual del proyecto.
  - TASKS: tareas pendientes o realizadas
  - BUGS: errores encontrados o problemas que surguieron durante la sesión.
  - SOLUTIONS: soluciones encontradas o propuestas para resolver los problemas problemas y el por qué se implementó de esa forma.

## CONFIRMACIÓN
Después de hacer el backup en engram, siempre se debe notificar a Gustavo, indicando que se escribió en dichas notas.
