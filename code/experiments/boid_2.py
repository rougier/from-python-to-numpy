# FAST BOIDS
"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

boids_x=np.array([random.uniform(-450,50.0) for x in range(50)])
boids_y=np.array([random.uniform(300.0,600.0) for x in range(50)])
boid_x_velocities=np.array([random.uniform(0,10.0) for x in range(50)])
boid_y_velocities=np.array([random.uniform(-20.0,20.0) for x in range(50)])

def update_boids(xs, ys, xvs, yvs):
    xdiff = np.add.outer(xs,-xs)
    ydiff = np.add.outer(ys,-ys)
        
    xvdiff = np.add.outer(xvs,-xvs)
    yvdiff = np.add.outer(yvs,-yvs)
    distance=xdiff**2+ydiff**2
    cond1=distance < 100
    cond2=distance < 10000
        
    xvs += np.sum(xdiff[:,],axis=0)*0.01/50
    yvs += np.sum(ydiff[:,],axis=0)*0.01/50
        
    yvs += -np.sum(xdiff[:,]*cond1,axis=0)
    xvs += -np.sum(ydiff[:,]*cond1,axis=0)

    # Replacing the below loop with this makes the code sigificantly faster but also slightly different.
    xvs += np.sum(xdiff[:,]*cond2,axis=0)*0.125/50
    yvs += np.sum(ydiff[:,]*cond2,axis=0)*0.125/50

# This is similar to the other codes but also much slower. It is included in case changes made are unacceptable. 
#	for i in range(50):
#		for j in range(50):
#			if distance[i,j] < 10000:
#				xvs[i]+=xvdiff[j,i]*0.125/50
#				yvs[i]+=yvdiff[j,i]*0.125/50
				
    xs += xvs
    ys += yvs			
                   

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids_x,boids_y)

def animate(frame):
   update_boids(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
   Z = np.vstack((boids_x,boids_y))
   print(Z.T.shape)
   scatter.set_offsets(Z.T) #zip(boids_x,boids_y))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
