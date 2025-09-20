# 🎯 Mejoras a los juegos

# Eder

## 📝 Descripción
Este documento describe las mejoras implementadas en el juego Cannon para hacer la experiencia más dinámica y continua.

## 🚀 Cambios Realizados

### 1. ⚡ Velocidad Aumentada del Proyectil
- **Archivo modificado**: `cannon.py`
- **Función afectada**: `tap(x, y)`
- **Cambio**: 
  - **Antes**: `speed.x = (x + 200) / 25` y `speed.y = (y + 200) / 25`
  - **Después**: `speed.x = (x + 200) / 15` y `speed.y = (y + 200) / 15`
- **Resultado**: El proyectil ahora se mueve **1.67x más rápido**

### 2. 🎯 Velocidad Aumentada de los Objetivos
- **Archivo modificado**: `cannon.py`
- **Función afectada**: `move()`
- **Cambio**:
  - **Antes**: `target.x -= 0.5`
  - **Después**: `target.x -= 1.5`
- **Resultado**: Los objetivos ahora se mueven **3x más rápido**

### 3. ♾️ Juego Infinito
- **Archivo modificado**: `cannon.py`
- **Función afectada**: `move()`
- **Cambios implementados**:

#### Eliminación de condición de fin de juego
```python
# CÓDIGO ELIMINADO:
for target in targets:
    if not inside(target):
        return  # Esta línea terminaba el juego
```

#### Nueva lógica de reposicionamiento
```python
# CÓDIGO AGREGADO:
repositioned_targets = []
for target in targets:
    if inside(target):
        repositioned_targets.append(target)
    else:
        # Si el objetivo sale por la izquierda, reposicionarlo por la derecha
        if target.x < -200:
            new_y = randrange(-150, 150)
            new_target = vector(200, new_y)
            repositioned_targets.append(new_target)

targets.clear()
targets.extend(repositioned_targets)
```

## 🎮 Cómo Funciona Ahora

1. **Proyectil más rápido**: Cuando haces clic en la pantalla, el cañón dispara proyectiles con mayor velocidad
2. **Objetivos más rápidos**: Los objetivos azules se mueven de derecha a izquierda más rápidamente
3. **Regeneración automática**: Cuando un objetivo sale por el lado izquierdo, automáticamente aparece uno nuevo por el lado derecho
4. **Sin fin de juego**: El juego continúa indefinidamente, proporcionando una experiencia de juego continua

## 🎮 Controles
- **Click en pantalla**: Dispara el proyectil hacia la posición del cursor
- **Objetivo**: Impactar los círculos azules con el proyectil rojo

## 🔄 Próximas Mejoras Sugeridas
1. ✅ ~~Aumentar velocidad de proyectiles y objetivos~~
2. ✅ ~~Implementar juego infinito~~
3. 🔲 Sistema de puntuación
4. 🔲 Efectos de sonido
5. 🔲 Diferentes tipos de objetivos
6. 🔲 Power-ups especiales
7. 🔲 Niveles de dificultad progresiva

# Cambios Vale 
---

## 📌 Cambios realizados

1. *Movimiento aleatorio de la comida*
   - La comida ahora se mueve un paso (10 px) en una dirección aleatoria (arriba, abajo, izquierda o derecha).
   - No se sale de la ventana ni se coloca sobre la víbora.

2. *Colores aleatorios*
   - Al iniciar el juego, la víbora y la comida reciben *colores diferentes* entre sí.
   - Los colores son elegidos aleatoriamente de una paleta de 5 (blue, green, orange, purple, yellow), *excluyendo el rojo*.

3. *Documentación*
   - Se añadieron *docstrings* y comentarios en español para facilitar el entendimiento y cumplir con el estándar de documentación del Instituto.

---

## 🎮 Instrucciones de ejecución

### 1. Requisitos
- Python 3.x instalado en tu sistema.
- Librería [freegames](https://pypi.org/project/freegames/).

# Cambios Rafa

Cambio de Tablero:
### 1. Cambio en el tablero
Se modificó la lista tiles para crear un nuevo mapa. 

Cambio de Tablero:
### 2. Cambio en la velocidad de los fantasmas
Se aumentó la velocidad de los fantasmas de 5 a 10, tanto en su definición inicial como en sus movimientos aleatorios.
- [vector(-180, 160), vector(5, 0)],
+ [vector(-180, 160), vector(10, 0)],

- vector(5, 0),
+ vector(10, 0),
