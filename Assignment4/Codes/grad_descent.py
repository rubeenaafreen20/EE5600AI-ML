# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:51:07 2020
4x^2+4x+4
@author: Rubeena
"""

import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex
from coeffs import *
import math


def f(x,a,b,d):
	return a*(x**2)+b*x+d

#Parabola parameters
a = 4
b = -4
d = 4

#Gradient Descent
cur_x = 1 # The algorithm starts at x=1
gamma = 0.001 # step size multiplier (learning rate)
precision = 0.00000001      #This tells us when to stop the algorithm
previous_step_size = 1 
max_iters = 100000000 # maximum number of iterations
iters = 0 #iteration counter

df = lambda x: 2*a*x + b            #gradient of the function

while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cur_x              #Store current x-value in orevious x
    cur_x -= gamma * df(prev_x)     #Gradient descent
    previous_step_size = abs(cur_x - prev_x)    #change in x
    iters+=1        #Go to next iteration
print(f(cur_x,a,b,d))
print("The local minimum occurs at", cur_x)

# equation - 4x^2-4x+4
x=np.linspace(0,1,40)
y=4*(x**2)-4*x+4
plt.plot(x,y);
plt.plot(cur_x,f(cur_x,a,b,d),'o')
plt.text(cur_x*(1+0.1), f(cur_x,a,b,d),'P')
plt.title("Parabola curve")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid()
plt.show()