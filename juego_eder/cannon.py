"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Aumentar la velocidad del proyectil multiplicando por un factor mayor
        speed.x = (x + 200) / 15  # Era /25, ahora /15 para más velocidad
        speed.y = (y + 200) / 15  # Era /25, ahora /15 para más velocidad


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Aumentar la velocidad de movimiento de los objetivos
    for target in targets:
        target.x -= 1.5  # Era -0.5, ahora -1.5 para más velocidad

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    # Reposicionar objetivos que salen de la pantalla en lugar de terminar el juego
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

    draw()

    # Continuar el juego siempre (remover la condición que terminaba el juego)
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()