import pygame as pg
import math

vec = pg.math.Vector2

pos = vec(35,35).length()

x = vec(6, 1)
y = vec(2, 3)

z = x.normalize()

v = 0.3674
v2 = v**2

rot = (x - y).angle_to(vec(1, 0))

b = vec(1, 0).rotate(-rot)
print(b)

b.scale_to_length(5)
print(b)

t2 = vec(b[0]*1, b[1]*1)


print(t2)

