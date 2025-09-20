"""
Snake — juego clásico (versión modificada)

Modificaciones realizadas:
- La comida se mueve un paso (10 px) en una dirección aleatoria (arriba/abajo/izq/der)
  cada vez que se actualiza el juego. No puede salirse de la ventana ni colocarse
  sobre la víbora.
- Al iniciar el juego, la víbora y la comida reciben colores diferentes elegidos
  aleatoriamente a partir de una paleta de 5 colores (rojo excluido).

Instrucciones:
- Requiere Python 3.x, turtle y el paquete `freegames`.
  Instalar freegames (si hace falta): pip install freegames
- Ejecutar: python snake.py

Notas de diseño:
- Área de juego definida por los límites usados en la función inside(): 
  -200 < x < 190 y -200 < y < 190 (coincide con el ejemplo original).
- Movimiento en cuadricula de 10 px.
- Para mover la comida se intenta elegir una dirección válida; si no se
  encuentra una (caso improbable) la comida permanece en su lugar.
"""

from random import randrange, choice, sample
from turtle import *

from freegames import square, vector

# --- Configuración de juego / constantes ---
GRID_STEP = 10  # tamaño del paso (pixeles)
BOUND_MIN = -200
BOUND_MAX = 190

# Paleta disponible (5 colores) — rojo queda excluido por requisito.
COLOR_PALETTE = ['blue', 'green', 'orange', 'purple', 'yellow']

# --- Estados del juego ---
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Elegir colores (aleatorios y distintos) para snake y food al iniciar.
snake_color, food_color = sample(COLOR_PALETTE, 2)


def change(x, y):
    """
    Cambia la dirección de movimiento de la víbora.
    Llamado por los eventos de teclado.
    """
    aim.x = x
    aim.y = y


def inside(head):
    """
    Devuelve True si la cabeza está dentro de los límites de la ventana.
    """
    return BOUND_MIN < head.x < BOUND_MAX and BOUND_MIN < head.y < BOUND_MAX


def valid_food_position(pos):
    """
    Verifica que la posición pos (vector) no esté sobre la víbora
    y esté dentro de los límites.
    """
    if not inside(pos):
        return False
    for segment in snake:
        if pos == segment:
            return False
    return True


def move_food_one_step():
    """
    Mueve la comida un paso (GRID_STEP) en una dirección cardinal aleatoria.
    Asegura que la nueva posición esté dentro de los límites y no coincida
    con la víbora. Intenta varias direcciones antes de quedarse.
    """
    directions = [(GRID_STEP, 0), (-GRID_STEP, 0), (0, GRID_STEP), (0, -GRID_STEP)]
    # Embarajar para no favorecer ninguna dirección
    from random import shuffle
    shuffle(directions)

    for dx, dy in directions:
        new_pos = vector(food.x + dx, food.y + dy)
        if valid_food_position(new_pos):
            food.x, food.y = new_pos.x, new_pos.y
            return
    # Si ninguna dirección válida (muy improbable), dejar la comida en su lugar.
    return


def move():
    """
    Mueve la víbora un segmento hacia adelante siguiendo 'aim'.
    - Si la víbora sale de los límites o se muerde a sí misma, termina el juego.
    - Si la cabeza llega a la comida, se come (crece) y se reubica la comida
      aleatoriamente en la grilla; de lo contrario, la víbora mantiene longitud.
    - Además, en cada tick, la comida se mueve un paso al azar (comportamiento añadido).
    """
    head = snake[-1].copy()
    head.move(aim)

    # Colisión con paredes o consigo misma -> fin de juego
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # cabeza en rojo para indicar choque
        update()
        return

    snake.append(head)

    if head == food:
        # Comido: crecer (no quitar cola) y reubicar comida aleatoriamente en la grilla
        print('Snake:', len(snake))
        # Reubicar la comida en una posición aleatoria válida dentro de la grilla.
        placed = False
        attempts = 0
        while not placed and attempts < 1000:
            new_x = randrange(-15, 15) * GRID_STEP
            new_y = randrange(-15, 15) * GRID_STEP
            candidate = vector(new_x, new_y)
            if valid_food_position(candidate):
                food.x, food.y = new_x, new_y
                placed = True
            attempts += 1
        # Si por algún motivo no se encontró posición, se deja la comida donde estaba.
    else:
        # No comió: avanzar (quitar la cola para mantener longitud)
        snake.pop(0)
        # Mover la comida un paso aleatorio cada tick (comportamiento requerido).
        move_food_one_step()

    # Dibujado
    clear()

    # Dibujar cuerpo de la víbora (todos los segmentos excepto la cabeza)
    for body in snake[:-1]:
        square(body.x, body.y, 9, snake_color)

    # Dibujar cabeza (para que destaque, usamos un borde más brillante — mismo color)
    head_segment = snake[-1]
    square(head_segment.x, head_segment.y, 9, snake_color)

    # Dibujar comida con el color asignado
    square(food.x, food.y, 9, food_color)

    update()
    # Llamar de nuevo a move después de 100 ms
    ontimer(move, 100)


# --- Inicialización ---
# Colocar la comida en una posición aleatoria inicial (y válida)
placed = False
while not placed:
    x = randrange(-15, 15) * GRID_STEP
    y = randrange(-15, 15) * GRID_STEP
    candidate = vector(x, y)
    if valid_food_position(candidate):
        food.x, food.y = x, y
        placed = True

# Setup de ventana / turtle
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Enlazar teclas de dirección
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Mensaje informativo en consola (opcional)
print(f"Colores: víbora={snake_color}, comida={food_color}")

# Inicia el bucle del juego
move()
done()