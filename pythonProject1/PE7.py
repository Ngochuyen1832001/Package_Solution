#A robot moves in a planet starting from the original point(0,0). The robot can move UP, DOWN, LEFT, RIGHT
#UP:5 DOWN:3 LEFT:3 RIGHT:2
#The num after direction are steps. Compute the distance from current position after a sequence of movement and original point.
#distance float -> print nearest integer

import math

xS, yS = 0, 0
xE, yE = xS, yS


def up(step, x, y):
    y += step
    return x, y


def down(step, x, y):
    y -= step
    return xE, y


def left(step, x, y):
    x -= step
    return x, y


def right(step, x, y):
    x += step
    return x, y


xE, yE = up(5, xE, yE)
xE, yE = down(3, xE, yE)
xE, yE = left(3, xE, yE)
xE, yE = right(2, xE, yE)


def calDistance(x1, y1, x2, y2):
    return math.sqrt(pow((x1-x2), 2) + pow((y1-y2), 2))


print(calDistance(xS, yS, xE, yE))

#A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN,
#LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3
#LEFT 3 RIGHT 2 ¡­ The numbers after the direction are steps. Please write a program to compute the distance
#from current position after a sequen…

import math

x, y = 0, 0

while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)