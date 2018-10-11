import math

import numpy as np

from utils import Shape, Sphere
from vec import Vec


MAX_RAY = 10000

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def get_point(self, t):
        return self.origin + self.direction * t


class Scene(Shape):
    def __init__(self):
        super(Scene, self).__init__()
        self.shapes = list()

    def hit(self, ray, t_min, t_max):
        self.hits = []
        hit_anything = False
        closest = t_max
        for shape in self.shapes:
            (is_hit, hit) = shape.hit(ray, t_min, closest)
            if is_hit:
                hit_anything = True
                closest = hit.t
                self.hits.append(hit)

        # we return last hit since its the nearest
        return hit_anything, self.hits[-1] if hit_anything else 0


def color(ray, scene):
    (is_hit, hit) = scene.hit(ray, 0.0, MAX_RAY)
    if is_hit:
        return Vec(hit.normal.x + 1, hit.normal.y + 1, hit.normal.z + 1) * (1 / 3)
    dir = ray.direction.get_normalized()
    t = 0.5 * (dir.y + 1.0)  # the higher we are the higher our blue is gonna be = 1 if y = 1
    return Vec(1, 1, 1) * (1 - t) + Vec(.5, .7, 1) * t


def write_ppm():
    # cam and image properties
    N = 200
    M = 100

    lower_left_corner = Vec(-2, -1, -1)
    horizontal = Vec(4, 0, 0)
    vertical = Vec(0, 2, 0)
    origin = Vec(0, 0, 0)

    # construct scene
    scene = Scene()
    scene.shapes.append(Sphere(Vec(0, 0, -1), 0.5))
    scene.shapes.append(Sphere(Vec(0, -100.5, -1), 100))


    with open('first.ppm', 'w') as ppm:
        ppm.write('P3\n {} {}\n 255\n'.format(N, M))  # P3 magic, Cols Rows, 255 = max value
        for m in range(M):
            for n in range(N):
                u = n / N
                v = (M - m) / M

                r = Ray(origin, lower_left_corner + horizontal * u + vertical * v)
                col = color(r, scene)
                r = col.x
                g = col.y
                b = col.z
                ppm.write("{} {} {}\n".format(int(r * 255), int(g * 255), int(b * 255)))


if __name__ == '__main__':
    print("starting")
    write_ppm()
