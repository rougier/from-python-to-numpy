# Matplotlib / individual rotation markers using a single path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.animation import FuncAnimation
from matplotlib.collections import PathCollection


triangle = [[(-0.25, -0.5), (+0.0, +0.5), (+0.25, -0.5), (+0.0, +0.0)],
            [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]]


class MarkerCollection:
    def __init__(self, n=100, marker=triangle):
        v, c = marker
        v, c = np.array(v), np.array(c)
        self._marker = marker
        self._base_vertices = np.tile(v.reshape(-1), n).reshape(n, len(v), 2)
        self._vertices = np.tile(v.reshape(-1), n).reshape(n, len(v), 2)
        self._codes = np.tile(c.reshape(-1), n)
        self._scale = np.ones(n)
        self._translate = np.zeros((n, 2))
        self._rotate = np.zeros(n)
        self._path = Path(vertices=self._vertices.reshape(n*len(v), 2),
                          codes=self._codes)
        self._collection = PathCollection(
            [self._path], facecolor="white", edgecolor="black")

    def __len__(self):
        return len(self._base_vertices)

    def scale(self, scale):
        self._scale = scale

    def translate(self, translate):
        self._translate = translate.reshape(len(self), 1, 2)

    def rotate(self, rotate):
        self._rotate = rotate

    def update(self):
        n = len(self)

        # Scale
        self._vertices[...] = self._base_vertices * self._scale

        # Rotation
        cos_rotate, sin_rotate = np.cos(self._rotate), np.sin(self._rotate)
        R = np.empty((n, 2, 2))
        R[:, 0, 0] = cos_rotate
        R[:, 1, 0] = sin_rotate
        R[:, 0, 1] = -sin_rotate
        R[:, 1, 1] = cos_rotate
        self._vertices[...] = np.einsum('ijk,ilk->ijl', self._vertices, R)

        # Translation
        self._vertices += self._translate

fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(1, 1, 1, aspect=1)

n = 750
collection = MarkerCollection(n)
collection.scale(0.025)
collection.rotate(np.linspace(0, 2*np.pi, n, endpoint=False))
radius = 0.75
angle = np.linspace(0, 2*np.pi, n, endpoint=False)
xy = np.dstack((radius*np.cos(angle), radius*np.sin(angle)))

collection.translate(np.random.uniform(-1,1,(n,2)))
collection.update()

ax.add_collection(collection._collection)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

def update(*args):
    collection._rotate += np.pi/50
    collection.update()

animation = FuncAnimation(fig, update, interval=10)
plt.show()
