# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 09:45:42 2018

@author: lil-apu
"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

print('please wait a moment...')

plt.rcParams['font.sans-serif']=['SimHei'] # 正常显示中文
plt.rcParams['axes.unicode_minus']=False   # 正常显示负号

fig = plt.figure()
ax = Axes3D(fig)
plt.xticks(np.linspace(-0.8,0.8,6),['用','我','三','生','烟','火'])
plt.yticks(np.linspace(-0.8,0.8,6),['换','你','一','世','迷','离'])

X,Y = np.array(range(25))/24.0, np.arange(0, 575.5, 0.5)/575*17*np.pi-2*np.pi
[X, Y] = np.meshgrid(X,Y)
a = (np.pi/2)*np.exp(-Y/(8*np.pi))
b = 1-(1-np.mod(3.6*Y, 2*np.pi)/np.pi)**4/2
c = 2*(X**2-X)**2*np.sin(a)
d = b*(X*np.sin(a)+c*np.cos(a))

x,y,z = d*np.cos(Y), d*np.sin(Y), b*(X*np.cos(a)-c*np.sin(a))

surf = ax.plot_surface(x,y,z,rstride=1,cstride=1, 
                       cmap=cm.gist_rainbow_r,linewidth=0, antialiased=True)

plt.show()

