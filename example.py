from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import ROOT
from array import array

rechits=[]

recfile=ROOT.TFile('savehits_output_1.root','READ')
myTree = recfile.Get("hits_tree")
n=0
for entry in myTree:
	n=n+1
	if n==3:
		break
	for i in range(len(entry.hit_global_x)): 
		rechits.append([entry.hit_global_x[i],entry.hit_global_y[i],entry.hit_global_z[i]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

rechits_t=list(map(list, zip(*rechits)))

xs = array( 'd' , rechits_t[0])
ys = array( 'd' , rechits_t[1])
zs = array( 'd' , rechits_t[2])
ax.scatter(zs, xs, ys, c='b',alpha=0.2, marker='.',s=1)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
