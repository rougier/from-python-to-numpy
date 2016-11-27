import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.animation import FuncAnimation
from matplotlib.collections import PathCollection


class MarkerCollection:
    def __init__(self, n=100):
        v = np.array([(-0.25, -0.25), (+0.0, +0.5), (+0.25, -0.25), (+0.0, +0.0)])
        c = np.array([Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY])
        self._base_vertices = np.tile(v.reshape(-1), n).reshape(n, len(v), 2)
        self._vertices = np.tile(v.reshape(-1), n).reshape(n, len(v), 2)
        self._codes = np.tile(c.reshape(-1), n)
        self._scale = np.ones(n)
        self._translate = np.zeros((n, 2))
        self._rotate = np.zeros(n)
        self._path = Path(vertices=self._vertices.reshape(n*len(v), 2), codes=self._codes)
        self._collection = PathCollection([self._path], facecolor="white", edgecolor="black")

    def update(self):
        n = len(self._base_vertices)
        self._vertices[...] = self._base_vertices * self._scale
        cos_rotate, sin_rotate = np.cos(self._rotate), np.sin(self._rotate)
        R = np.empty((n, 2, 2))
        R[:, 0, 0] = cos_rotate
        R[:, 1, 0] = sin_rotate
        R[:, 0, 1] = -sin_rotate
        R[:, 1, 1] = cos_rotate
        self._vertices[...] = np.einsum('ijk,ilk->ijl', self._vertices, R)
        self._vertices += self._translate.reshape(n, 1, 2)


class Flock:
    def __init__(self, count=500, width=640, height=360):
        self.width = width
        self.height = height
        self.max_velocity = 2
        self.max_acceleration = 0.03
        angle = np.random.uniform(0, 2*np.pi, count)
        self.velocity = np.vstack((np.cos(angle), np.sin(angle))).T
        self.position = np.random.uniform(-100, 100, (count, 2)) + (width/2, height/2)
        self.position = self.position.astype(np.float32)
        self.velocity = self.velocity.astype(np.float32)

    def run(self):
        position = self.position
        velocity = self.velocity
        max_velocity = self.max_velocity
        max_acceleration = self.max_acceleration
        n = len(position)

        dx = np.subtract.outer(position[:, 0], position[:, 0])
        dy = np.subtract.outer(position[:, 1], position[:, 1])
        distance = np.hypot(dx, dy)

        # Compute common distance masks
        mask_0 = (distance > 0)
        mask_1 = (distance < 25)
        mask_2 = (distance < 50)
        mask_1 *= mask_0
        mask_2 *= mask_0
        mask_3 = mask_2
        mask_1_count = np.maximum(mask_1.sum(axis=1), 1)
        mask_2_count = np.maximum(mask_2.sum(axis=1), 1)
        mask_3_count = mask_2_count

        # Separation
        # -----------------------------------------------------------------------------
        # Compute target
        mask, count = mask_1, mask_1_count
        target = np.dstack((dx, dy))
        target = np.divide(target, distance.reshape(n, n, 1)**2, out=target,
                           where=distance.reshape(n, n, 1) != 0)

        # Compute steering
        steer = (target*mask.reshape(n, n, 1)).sum(axis=1)/count.reshape(n, 1)
        norm = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        steer = max_velocity*np.divide(steer, norm, out=steer,
                                       where=norm != 0)
        steer -= velocity

        # Limit acceleration
        norm = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        steer = np.multiply(steer, max_acceleration/norm, out=steer,
                            where=norm > max_acceleration)

        separation = steer

        # Alignment
        # -----------------------------------------------------------------------------
        # Compute target
        mask, count = mask_2, mask_2_count
        target = np.dot(mask, velocity)/count.reshape(n, 1)

        # Compute steering
        norm = np.sqrt((target*target).sum(axis=1)).reshape(n, 1)
        target = max_velocity * np.divide(target, norm, out=target,
                                          where=norm != 0)
        steer = target - velocity

        # Limit acceleration
        norm = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        steer = np.multiply(steer, max_acceleration/norm, out=steer,
                            where=norm > max_acceleration)
        alignment = steer

        # Cohesion
        # -----------------------------------------------------------------------------
        # Compute target
        mask, count = mask_3, mask_3_count
        target = np.dot(mask, position)/count.reshape(n, 1)

        # Compute steering
        desired = target - position
        norm = np.sqrt((desired*desired).sum(axis=1)).reshape(n, 1)
        desired *= max_velocity / norm
        steer = desired - velocity

        # Limit acceleration
        norm = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        steer = np.multiply(steer, max_acceleration/norm, out=steer,
                            where=norm > max_acceleration)
        cohesion = steer

        # -----------------------------------------------------------------------------
        acceleration = 1.5 * separation + alignment + cohesion
        velocity += acceleration

        norm = np.sqrt((velocity*velocity).sum(axis=1)).reshape(n, 1)
        velocity = np.multiply(velocity, max_velocity/norm, out=velocity,
                               where=norm > max_velocity)
        position += velocity

        # Wraparound
        position[...] = (position + (self.width, self.height)) % (self.width, self.height)


def update(*args):
    flock.run()
    collection._scale = 8
    collection._translate = flock.position
    collection._rotate = np.arctan2(flock.velocity[:,1],flock.velocity[:,0])-np.pi/2
    collection.update()
    
    # scatter.set_offsets(flock.position)
    
    

n = 500
flock = Flock(n)
fig = plt.figure(figsize=(12, 6))
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=True)

#scatter = ax.scatter(flock.position[:, 0], flock.position[:, 1],
#                     s=15, facecolor="red", edgecolor="None", alpha=0.5)

collection = MarkerCollection(n)
ax.add_collection(collection._collection)

animation = FuncAnimation(fig, update, interval=10)
ax.set_xlim(0, 640)
ax.set_ylim(0, 360)
ax.set_xticks([])
ax.set_yticks([])
plt.show()
