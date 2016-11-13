# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def display_2D_array(ax, Z, origin="upper"):

    rows, columns = Z.shape

    fontsize = 10 * 8.0/max(rows,columns)
    
    ax.set_xlim(0, columns)
    ax.set_xticks(np.arange(1, columns))
    ax.set_ylim(0, rows)
    ax.set_yticks(np.arange(1, rows))
    ax.grid(color="0.25", linestyle="-", linewidth=0.5, alpha=0.5)
    
    for tick in ax.xaxis.get_major_ticks():
        tick.tick1On = tick.tick2On = False
    ax.set_xticklabels([])
    for tick in ax.yaxis.get_major_ticks():
        tick.tick1On = tick.tick2On = False
    ax.set_yticklabels([])

    for y in range(rows):
        for x in range(columns):
            text = str(Z[y,x])
            if origin == "upper":
                ax.text(x+0.5, rows-y-0.5, text, fontsize=fontsize,
                         horizontalalignment="center", verticalalignment="center")
            else:
                ax.text(x+0.5, y+0.5, text, fontsize=fontsize,
                         horizontalalignment="center", verticalalignment="center")

    

def display(base, view, label, dx, dy):

    fig = plt.figure(figsize=(10,5.5))
    origin = "upper"
    _base = base.copy()
    _view = view.copy()

    itemsize = view.itemsize
    offset_start = (np.byte_bounds(view)[0] - np.byte_bounds(base)[0])//itemsize
    offset_stop = (np.byte_bounds(view)[-1] - np.byte_bounds(base)[-1]-1)//itemsize
    index_start = np.array(np.unravel_index(offset_start, base.shape))
    index_stop = np.array(np.unravel_index(base.size+offset_stop, base.shape))

    
    # Base
    # ---------------------------------
    ax1 = plt.subplot(1, 2, 1, aspect=1)
    display_2D_array(ax1, _base, origin)
    ax1.set_title("base", family="Menlo")

    rows, columns = base.shape
    base[...], view[...] = 0, 1
    plt.imshow(base, extent=[0,columns, 0, rows], vmin=0, vmax=8,
               interpolation = "nearest", cmap="gray_r", origin=origin)

    y, x = index_start
    h, w = index_stop - index_start + 1
    if origin == "upper":
        y = base.shape[0] - y - h
    rect = patches.Rectangle((x,y), width=w, height=h,
                             linewidth=1.5, linestyle='--',
                             edgecolor='k', facecolor='none',
                             transform=ax1.transData)
    ax1.add_patch(rect)


    ox = x
    oy = y
    d = 1
    arrowprops={"width": .5,
                "headlength": 6.0,
                "headwidth": 6.0,
                "facecolor": "black",
                "shrink": 0.0}

    if dx > 0: x0, x1,x2 = ox, ox+d, ox
    else:      x0, x1, x2 = w+ox, w+ox-d, w+ox
    if dy > 0: y0, y1,y2 = h+oy, h+oy-d, h+oy
    else:      y0, y1, y2 = oy, oy+d, oy
    ax1.annotate("", arrowprops=arrowprops,
                 xy=(x1, y0),  xycoords='data',
                 xytext=(x2, y0), textcoords='data')
    ax1.annotate("", arrowprops=arrowprops,
                 xy=(x0, y1),  xycoords='data',
                 xytext=(x0, y2), textcoords='data')
    plt.scatter([x0], [y0], s=50, facecolor="white", edgecolor="black", zorder=10)
    
    
    # View
    # ---------------------------------
    ax2 = plt.subplot(1, 2, 2, aspect=1)
    display_2D_array(ax2, _view, origin)
    ax2.set_title("view = base[%s]" % label, family="Menlo")

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    base = np.arange(9*9).reshape(9,9)

    # view = base[-2:1:-2,-2:1:-2]
    # display(base, view, "-2:1:-2,-2:1:-2", -1, -1)

    view = base[1:-1:2, 1:-1:2]
    display(base, view, "1:-1:2, 1:-1:2", +1, +1)
