"""
一位销售员计划在欧洲进行商务之旅，他需要访问5个城市：巴黎（法国）、柏林（德国）、罗马（意大利）、马德里（西班牙）和伦敦（英国）。为了节省时间和成本，他希望找到一条旅行路线，使得总旅行距离最短。已知各城市之间的距离如下（单位：千米）：
0 1050 1420 1270 460
1050 0 1200 240 1100
1420 1200 0 1950 1760
1270 240 1950 0 1270
460 1100 1760 1270 0
请帮助这位销售员找到一条访问所有城市并回到起点的最短路径。
输入格式：
第1行：一个整数 n（5 <= n <= 10），表示城市数量。
接下来的n行：每行包含n个整数，表示城市之间的距离矩阵。
输出格式：
输出一个整数，表示总行程的最短距离。
"""
import cvxpy as cp
import numpy as np
n=int(input().strip())
dist_matrix=np.zeros((n,n))
for i in range(n):
    row=list(map(int,input().strip().split()))
    for j in range(n):
        dist_matrix[i,j]=row[j]
x=cp.Variable((n,n),boolean=True)
u=cp.Variable(n,integer=True)
objective=cp.Minimize(cp.sum(cp.multiply(dist_matrix,x)))
constraints=[]
for i in range(n):
    constraints.append(cp.sum(x[i,:])==1)
    constraints.append(cp.sum(x[:,i])==1)
for i in range(1,n):
    for j in range(1,n):
        constraints.append(u[i]-u[j]+n*x[i,j]<=n-1)
prob=cp.Problem(objective,constraints)
result=prob.solve('GLPK_MI')
print(int(result))