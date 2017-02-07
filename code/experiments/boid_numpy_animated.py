import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Flock:
    def __init__(self, count=500, width=640, height=360):
        self.width = width
        self.height = height
        self.max_velocity = 2
        self.max_acceleration = 0.03
        self.r = 2
        angle = np.random.uniform(0, 2*np.pi, count)
        self.velocity = np.vstack((np.cos(angle), np.sin(angle))).T
        self.position = np.random.uniform(-1, 1, (count, 2)) + (width/2, height/2)

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
        mask_25 = (distance < 20)
        mask_50 = (distance < 50)
        mask_0_25 = mask_0 * mask_25
        mask_0_50 = mask_0 * mask_50
        mask_0_25_count = np.maximum(mask_0_25.sum(axis=1), 1)
        mask_0_50_count = np.maximum(mask_0_50.sum(axis=1), 1)

        # Separation
        # -----------------------------------------------------------------------------
        # Compute target
        mask, count = mask_0_25, mask_0_25_count
        target = np.dstack((dx, dy))
        target = np.divide(target, distance.reshape(n, n, 1)**2, out=target,
                           where=distance.reshape(n, n, 1) != 0)

        # Compute steering
        steer = (target*mask.reshape(n, n, 1)).sum(axis=1)/count.reshape(n, 1)
        norm_1 = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        steer = max_velocity * np.divide(steer, norm_1, out=steer, where=norm_1 != 0)
        steer -= velocity

        # Limit acceleration
        norm_1 = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        norm_2 = np.minimum(norm_1, max_acceleration)
        steer = np.multiply(steer, norm_2/norm_1, out=steer, where=norm_1 != 0)
        separation = steer

        # Alignment
        # -----------------------------------------------------------------------------
        # Compute target
        mask, count = mask_0_50, mask_0_50_count
        target = np.dot(mask, velocity)/count.reshape(n, 1)

        # Compute steering
        norm = np.sqrt((target*target).sum(axis=1)).reshape(n, 1)
        target = max_velocity * np.divide(target, norm, out=target, where=norm != 0)
        steer = target - velocity

        # Limit acceleration
        norm_1 = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        norm_2 = np.minimum(norm_1, max_acceleration)
        steer = np.multiply(steer, norm_2/norm_1, out=steer, where=norm_1 != 0)
        alignment = steer

        # Cohesion
        # -----------------------------------------------------------------------------
        # Compute target
        mask, count = mask_0_50, mask_0_50_count
        target = np.dot(mask, position)/count.reshape(n, 1)

        # Compute steering
        desired = target - position
        norm = np.sqrt((desired*desired).sum(axis=1)).reshape(n, 1)
        desired *= max_velocity / norm
        steer = desired - velocity

        # Limit acceleration
        norm_1 = np.sqrt((steer*steer).sum(axis=1)).reshape(n, 1)
        norm_2 = np.minimum(norm_1, max_acceleration)
        steer = np.multiply(steer, norm_2/norm_1, out=steer, where=norm_1 != 0)
        cohesion = steer

        # -----------------------------------------------------------------------------
        acceleration = 1.5 * separation + alignment + cohesion
        velocity += acceleration
        norm_1 = np.sqrt((velocity*velocity).sum(axis=1)).reshape(n, 1)
        norm_2 = np.minimum(norm_1, max_velocity)
        velocity = np.multiply(velocity, norm_2/norm_1, out=velocity, where=norm_1 != 0)
        position += velocity
        
        # Wraparound
        position[...] = (position + (self.width, self.height)) % (self.width, self.height)


def update(*args):
    flock.run()
    scatter.set_offsets(flock.position)

flock = Flock(1000)
fig = plt.figure(figsize=(8, 5))
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=True)
scatter = ax.scatter(flock.position[:, 0], flock.position[:, 1],
                     s=5, facecolor="red", edgecolor="None", alpha=0.5)
animation = FuncAnimation(fig, update, interval=10)
ax.set_xlim(0, 640)
ax.set_ylim(0, 360)
ax.set_xticks([])
ax.set_yticks([])
plt.show()
