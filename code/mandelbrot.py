# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# -----------------------------------------------------------------------------
import numpy as np

def mandelbrot_1(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    def mandelbrot(z,maxiter):
        c = z
        for n in range(maxiter):
            if abs(z) > horizon:
                return n
            z = z*z + c
        return maxiter
    r1 = [xmin+i*(xmax-xmin)/xn for i in range(xn)]
    r2 = [ymin+i*(ymax-ymin)/yn for i in range(yn)]
    return [mandelbrot(complex(r, i),maxiter) for r in r1 for i in r2]


def mandelbrot_2(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    def mandelbrot(C, maxiter, horizon=4.0):
        N = np.zeros(C.shape, dtype=int)
        Z = np.zeros(C.shape, np.complex64)
        for n in range(maxiter):
            I = np.less(abs(Z), horizon)
            N[I] = n
            Z[I] = Z[I]**2 + C[I]
        N[N == maxiter-1] = 0
        return Z, N

    X = np.linspace(xmin, xmax, xn, dtype=np.float32)
    Y = np.linspace(ymin, ymax, yn, dtype=np.float32)
    C = X + Y[:,None]*1j

    # Normalized recount as explained in:
    # http://linas.org/art-gallery/escape/smooth.html
    # and https://www.ibm.com/developerworks/community/blogs/jfp/entry/My_Christmas_Gift?lang=en
    Z, N = mandelbrot(C, maxiter, horizon)
    return Z, N


if __name__ == '__main__':
    from matplotlib import colors
    import matplotlib.pyplot as plt
    from tools import print_timeit

    xmin, xmax, xn = -2.25, +0.75, 3000/2
    ymin, ymax, yn = -1.25, +1.25, 2500/2
    maxiter = 200
    
    # print_timeit("mandelbrot_1(xmin, xmax, ymin, ymax, xn, yn, maxiter)", globals())
    # print_timeit("mandelbrot_2(xmin, xmax, ymin, ymax, xn, yn, maxiter)", globals())

    horizon = 2.0 ** 40
    log_horizon = np.log(np.log(horizon))/np.log(2)
    Z, N = mandelbrot_2(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)


    dpi = 72
    width = 10
    height = 10*yn/xn
    
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

    M = np.nan_to_num(N + 1 - np.log(np.log(abs(Z)))/np.log(2) + log_horizon)
    light = colors.LightSource(azdeg=315, altdeg=10)
    plt.imshow(light.shade(M, cmap=plt.cm.hot, vert_exag=1.5,
                           norm = colors.PowerNorm(0.3), blend_mode='hsv'),
               extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(xmin+0.025, ymin+0.025,
            "The Mandelbrot fractal set\n"
            "Rendered with matplotlib 2.0, 2016 — http://www.matplotlib.org",
            color="white", fontsize=12, alpha=0.5, family = "Source Sans Pro Light")
    plt.savefig("mandelbrot.png")
    plt.show()

