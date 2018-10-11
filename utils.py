import math

import numpy as np


class Hit:
    def __init__(self, t, p, normal):
        self.t = t
        self.p = p
        self.normal = normal.get_normalized()


class Shape:
    def __init__(self):
        pass

    def hit(self, ray, t_min, t_max):
        pass  # returns Hit


class Sphere(Shape):
    def __init__(self, center, radius):
        super(Sphere, self).__init__()
        self.center = center
        self.radius = radius

    def hit(self, ray, t_min, t_max):
        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = oc.dot(ray.direction) * 2.0
        c = oc.dot(oc) - self.radius * self.radius
        discr = b * b - 4 * a * c
        if discr > 0:
            temp = (-b - math.sqrt(discr)) / a
            if t_max > temp > t_min:
                p = ray.get_point(temp)
                return True, Hit(temp, p, (p - self.center) / self.radius)
            temp = (-b + math.sqrt(discr)) / a
            if t_max > temp > t_min:
                p = ray.get_point(temp)
                return True, Hit(temp, p, (p - self.center) / self.radius)
        return False, 0
