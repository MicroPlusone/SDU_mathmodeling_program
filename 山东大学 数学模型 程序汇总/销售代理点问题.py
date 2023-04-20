"""
现有7个社区，其相邻关系如下表示：
用aij表示第i个区和第j个区是否相邻：aij=1表示第i个区和第j个区相邻，aij=0表示第i个区和第j个区不相邻，其中i=1,⋯,7,j=1,⋯,7。相邻矩阵表示如下：
0,1,1,0,0,0,0
0,0,1,1,1,0,0
0,0,0,1,0,0,0
0,0,0,0,1,1,1
0,0,0,0,0,1,0
0,0,0,0,0,0,1
0,0,0,0,0,0,0
7个每个社区大学生的数量分别为34, 29, 42, 21, 56, 18, 71。现需要在7个区中选择两个区建立销售代理点，销售代理点可以向本区和一个相邻区的大学生售书。请建立数学优化模型，求出在哪两个区建立销售代理点可以使得能够供应的大学生数量最大。
输入格式:
第1行输入一个树，n, 表示方阵的大小
第2行到n+1行，表示n*n的相邻矩阵
最后一行表示人数
"""
import cvxpy as cp
import numpy as np
n=int(input())
a=np.zeros((n,n))
for i in range(n):
    a[i,:]=[eval(x) for x in input().split(',')]
r=[eval(x) for x in input().split(',')]
s=np.zeros((n,n))
for i in range(7):
    for j in range(7):
        s[i][j]=r[i]+r[j]
x=cp.Variable((n,n),boolean=True)
obj=cp.Maximize(cp.sum(cp.multiply(s,x)))
constraints=[]
con1=x<=a
constraints.append(con1)
con2=cp.sum(x,axis=1,keepdims=False)+cp.sum(x,axis=0,keepdims=False)<=1
constraints.append(con2)
con3=cp.sum(x)==2
constraints.append(con3)
prob=cp.Problem(obj,constraints)
prob.solve(solver='GLPK_MI')
print(int(prob.value))