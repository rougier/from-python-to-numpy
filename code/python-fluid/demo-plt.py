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

mouse = {"ox": 0.0, "oy": 0.0,
         "x": 0.0,  "y": 0.0,
         "button": None}


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

def user_step(d, u, v):
    global mouse

    d[:, :] = 0.0
    u[:, :] = 0.0
    v[:, :] = 0.0

    if mouse["button"] not in [1,3]:
        return

    i = int(mouse["y"]*N) + 1
    j = int(mouse["x"]*N) + 1

    if not 0 < i < N+1 and not 0 < j < N+1:
        return
    if mouse["button"] == 1:
        u[i, j] = force * (mouse["x"] - mouse["ox"])*100
        v[i, j] = force * (mouse["oy"] - mouse["y"])*100
    elif mouse["button"] == 3:
        d[i, j] = source

    mouse["ox"] = mouse["x"]
    mouse["oy"] = mouse["y"]


def update(*args):
    global im, dens, dens_prev, u, u_prev, v, v_prev, N, visc, dt, diff

    user_step(dens_prev, u_prev, v_prev)
    vel_step(N, u, v, u_prev, v_prev, visc, dt)
    dens_step(N, dens, dens_prev, u, v, diff, dt)
    im.set_data(dens)
    # im.set_clim(vmin=0, vmax=V.max())

def on_button_press(event):
    global mouse
    mouse["ox"] = mouse["x"] = event.xdata
    mouse["oy"] = mouse["y"] = event.ydata
    mouse["button"] = event.button

def on_button_release(event):
    global mouse
    mouse["ox"] = mouse["x"] = event.xdata
    mouse["oy"] = mouse["y"] = event.ydata
    mouse["button"] = None

def on_motion(event):
    global mouse
    mouse["x"] = event.xdata
    mouse["y"] = event.ydata



if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    clear_data()

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)


    cid = fig.canvas.mpl_connect('button_press_event', on_button_press)
    cid = fig.canvas.mpl_connect('button_release_event', on_button_release)
    cid = fig.canvas.mpl_connect('motion_notify_event', on_motion)

    ax.set_xlim(0,1)
    ax.set_xticks([])
    ax.set_ylim(0,1)
    ax.set_yticks([])

    im = ax.imshow(dens[1:-1,1:-1],
                   interpolation='bicubic', extent=[0,1,0,1],
                   cmap=plt.cm.gray, origin="lower", vmin=0, vmax=1)
    
    animation = FuncAnimation(fig, update, interval=10)
    plt.show()
