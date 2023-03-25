import math

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** (1/2)

def distEntity(entity1, entity2):
    return dist(entity1.x, entity1.y, entity2.x, entity2.y)

def direction(fromX, fromY, targetX, targetY):
    dy = -(targetY - fromY)
    dx = targetX - fromX
    if targetX >= fromX:
        if targetY <= fromY:
            quadrant = 1

        else:
            quadrant = 4

    else:
        if targetY <= fromY:
            quadrant = 2

        else:
            quadrant = 3
    if dx == 0:
        dx = 0.01

    dir = math.atan(dy / dx)
    pi = math.pi
    if quadrant == 1:
        direction = math.degrees(dir)

    elif quadrant == 2:
        direction = math.degrees(pi + dir)

    elif quadrant == 3:
        direction = math.degrees(pi + dir)

    else:
        direction = math.degrees(2 * pi + dir)

    return direction

def nearest_90(degree):
    if degree < 45 or degree > 315:
        return "e"

    elif degree > 45 and degree < 135:
        return "n"

    elif degree > 135 and degree < 225:
        return "w"

    else:
        return "s"