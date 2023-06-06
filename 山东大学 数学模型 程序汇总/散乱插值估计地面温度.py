import numpy as np
from scipy.interpolate import griddata
n,m=map(int,input().split())
known_points=[]
for i in range (n):
    x,y,t=map(float,input().split())
    known_points.append((x,y,t))
known_points=np.array(known_points)
query_points=[]
for i in range(m):
    x,y=map(float,input().split())
    query_points.append((x,y))
query_points=np.array(query_points)
interpolated_temps=griddata(known_points[:,:2],known_points[:,2],query_points,method='linear')
for temp in interpolated_temps:
    print("{:.2f}".format(temp))
