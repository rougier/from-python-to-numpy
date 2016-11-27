import math
from collections import namedtuple


def struct(name, members):
    cls = namedtuple(name, members)
    cls.__repr__ = lambda self: "%s(%s)" % (name, ','.join(str(s) for s in self))
    return cls


class vec2(struct('vec2', ('x', 'y'))):

    def __add__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x+other.x, self.y+other.y)
        return vec2(self.x+other, self.y+other)

    def __sub__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x-other.x, self.y-other.y)
        return vec2(self.x-other, self.y-other)

    def __mul__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x*other.x, self.y*other.y)
        return vec2(self.x*other, self.y*other)

    def __truediv__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x/other.x, self.y/other.y)
        return vec2(self.x/other, self.y/other)

    def length(self):
        return math.hypot(self.x, self.y)

    def normalized(self):
        length = self.length()
        if not length:
            length = 1.0
        return vec2(self.x/length, self.y/length)

    def limited(self, maxlength=1.0):
        length = self.length()
        if length > maxlength:
            return vec2(maxlength*self.x/length, maxlength*self.y/length)
        return self
