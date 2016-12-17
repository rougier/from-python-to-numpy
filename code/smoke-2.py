import numpy as np
from solver import vel_step, dens_step


N = 128
size = N + 2
dt = 0.1
diff = 0.0
visc = 0.0
force = 5.0
source = 100.0
dvel = False

u = np.zeros((size, size), np.float32)  # velocity
u_prev = np.zeros((size, size), np.float32)

v = np.zeros((size, size), np.float32)  # velocity
v_prev = np.zeros((size, size), np.float32)

dens = np.zeros((size, size), np.float32)  # density
dens_prev = np.zeros((size, size), np.float32)


def clear_data():
    """clear_data."""
    global u, v, u_prev, v_prev, dens, dens_prev, size

    u[:, :] = 0.0
    v[:, :] = 0.0
    u_prev[:, :] = 0.0
    v_prev[:, :] = 0.0
    dens[:, :] = 0.0
    dens_prev[:, :] = 0.0


    def disc(shape=(size,size), center=(size/2,size/2), radius = 10):
        def distance(x,y):
            return np.sqrt((x-center[0])**2+(y-center[1])**2)
        D = np.fromfunction(distance,shape)
        return np.where(D <= radius, True, False)

    D = disc(radius=10) - disc(radius=5)
    dens[...] += D*source/50
    
    D = disc(radius=20) - disc(radius=15)
    dens[...] += D*source/50
    
    ox, oy = size/2, size/2
    for j in range(1,N+1):
        for i in range(1,N+1):
            d = np.sqrt((i-ox)**2+(j-oy)**2)
            u[i,j] = (i-ox)/max(d,1) * force * 0.25
            v[i,j] = (j-oy)/max(d,1) * force * 0.25   
    u[:, :] += force * 0.1 * np.random.uniform(-1, 1, u.shape)
    v[:, :] += force * 0.1 * np.random.uniform(-1, 1, u.shape)



def update(*args):
    global im, dens, dens_prev, u, u_prev, v, v_prev, N, visc, dt, diff

    vel_step(N, u, v, u_prev, v_prev, visc, dt)
    dens_step(N, dens, dens_prev, u, v, diff, dt)
    im.set_data(dens)
    im.set_clim(vmin=dens.min(), vmax=dens.max())

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    clear_data()

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    ax.set_xlim(0, 1)
    ax.set_xticks([])
    ax.set_ylim(0, 1)
    ax.set_yticks([])

    im = ax.imshow(dens[1:-1, 1:-1],
                   interpolation='bicubic', extent=[0, 1, 0, 1],
                   cmap=plt.cm.gray, origin="lower", vmin=0, vmax=1)

    animation = FuncAnimation(fig, update, interval=10, frames=800)
    if 0:
        animation.save('smoke-2.mp4', fps=40, dpi=80, bitrate=-1,
                       codec="libx264", extra_args=['-pix_fmt', 'yuv420p'],
                       metadata={'artist': 'Nicolas P. Rougier'})
    plt.show()
