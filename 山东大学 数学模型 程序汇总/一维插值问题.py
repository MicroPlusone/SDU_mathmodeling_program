import numpy as np
from scipy.interpolate import interp1d
n=int(input())
data=[]
for _ in range(n):
    x,y=map(float,input().split())
    data.append([x,y])
data=np.array(data)
m=int(input())
x_pred=[]
for _ in range(m):
    x=float(input())
    x_pred.append(x)
x_pred=np.array(x_pred)
x_known=data[:,0]
y_known=data[:,1]
f=interp1d(x_known,y_known,kind='linear')
y_pred=f(x_pred)
for y in y_pred:
    print(f"{y:.2f}")
