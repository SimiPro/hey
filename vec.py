import numpy as np


class Vec:
    def __init__(self, x, y, z):
        self.vector = np.reshape(np.array([x, y, z], dtype=np.float32), (3, 1))
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_numpy(cls, v):
        if len(v) == 1:
            return v
        return cls(v[0], v[1], v[2])

    def get_normalized(self):
        norm = np.linalg.norm(self.vector)
        return Vec.from_numpy(self.vector / norm if not norm == 0 else self.vector)

    def dot(self, other):
        return np.dot(self.vector.T, other.vector)

    def get_norm(self):
        return np.linalg.norm(self.vector)


    def __truediv__(self, other):
        if type(other) is Vec:
            return Vec.from_numpy(self.vector / other.vector)
        return Vec.from_numpy(self.vector / other)

    def __add__(self, other):
        if type(other) is Vec:
            return Vec.from_numpy(self.vector + other.vector)
        return Vec.from_numpy(self.vector + other)

    def __sub__(self, other):
        if type(other) is Vec:
            return Vec.from_numpy(self.vector - other.vector)
        return Vec.from_numpy(self.vector - other)

    def __mul__(self, other):
        if type(other) is Vec:
            return Vec.from_numpy(self.vector * other.vector)
        return Vec.from_numpy(self.vector * other)

    def __str__(self):
        return "[{}, {}, {}]".format(self.x, self.y, self.z)
