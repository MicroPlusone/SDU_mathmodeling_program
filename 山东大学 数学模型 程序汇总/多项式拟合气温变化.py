import numpy as np
import scipy.optimize as opt
n,m=map(int,input().strip().split())
data_points=[]
for i in range(n):
    x,y=map(float,input().strip().split())
    data_points.append((x,y))
data_points=np.array(data_points)
coefficients=np.polyfit(data_points[:,0],data_points[:,1],m)
for i in coefficients:
    print("{:.2f}".format(i))
