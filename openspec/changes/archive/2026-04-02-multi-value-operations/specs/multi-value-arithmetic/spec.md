## ADDED Requirements

### Requirement: Suma de Múltiples Valores
El sistema SHALL realizar la suma de todos los elementos presentes en una lista de números de punto flotante.

#### Scenario: Suma exitosa de una serie de números
- **WHEN** se recibe la lista `[10.5, 20.0, 5.5, 4.0]`
- **THEN** el sistema retorna `40.0`

#### Scenario: Suma de lista vacía
- **WHEN** se recibe una lista vacía `[]`
- **THEN** el sistema retorna `0.0` (valor neutro de la suma)

### Requirement: Resta de Múltiples Valores
El sistema SHALL restar todos los elementos posteriores al primero de forma acumulativa.

#### Scenario: Resta exitosa de una serie de números
- **WHEN** se recibe la lista `[100.0, 20.0, 10.0]`
- **THEN** el sistema retorna `70.0` ($100.0 - 20.0 - 10.0$)

#### Scenario: Resta de un único elemento
- **WHEN** se recibe la lista `[50.0]`
- **THEN** el sistema retorna `50.0`

### Requirement: Multiplicación de Múltiples Valores
El sistema SHALL realizar el producto de todos los elementos presentes en una lista.

#### Scenario: Multiplicación exitosa de una serie de números
- **WHEN** se recibe la lista `[2.0, 3.0, 4.0]`
- **THEN** el sistema retorna `24.0`

#### Scenario: Multiplicación con un elemento cero
- **WHEN** se recibe la lista `[10.0, 0.0, 5.0]`
- **THEN** el sistema retorna `0.0`

### Requirement: División de Múltiples Valores
El sistema SHALL dividir el primer elemento por cada uno de los elementos subsiguientes de forma secuencial.

#### Scenario: División exitosa de una serie de números
- **WHEN** se recibe la lista `[100.0, 2.0, 5.0]`
- **THEN** el sistema retorna `10.0` ($100.0 / 2.0 = 50.0$; $50.0 / 5.0 = 10.0$)

#### Scenario: Error por división por cero en la secuencia
- **WHEN** se recibe la lista `[100.0, 5.0, 0.0, 2.0]`
- **THEN** el sistema lanza un error de tipo `ZeroDivisionError`
