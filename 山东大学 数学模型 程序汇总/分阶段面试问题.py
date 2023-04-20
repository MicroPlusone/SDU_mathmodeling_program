"""
有4名同学到一家公司参加三个阶段的面试：公司要求每个同学都必须首先找公司秘书初试，然后到部门主管处复试，最后到经理处参加面试，并且不允许插队（即在任何一个阶段4名同学的顺序是一样的）。由于4名同学的专业背景不同，所以每人在三个阶段的面试时间也不同，如下表所示（单位：分钟）：
秘书初试	主管复试	经理面试
同学甲	13	15	20
同学乙	10	20	18
同学丙	20	16	10
同学丁	8	10	15
这4名同学约定他们全部面试完以后一起离开公司。假定现在时间是早晨8:00，问他们最早何时能离开公司?
输入格式:
第1行输入两个数，m 表示同学数量，n表示阶段数
第2行到m+1行，表示m*n的矩阵, 是不同同学在不同阶段花费的时间
最后一行表示人数
输出格式:
从早晨8:00开始及时，到最后一名同学结束时，最少需要多少分钟，最终结果为整数。
"""
import cvxpy as cp
import numpy as np
m,n=[eval(x)for x in input().split(',')]
t=np.zeros((m,n))
for i in range(m):
    t[i,:]=[eval(x) for x in input().split(',')]
x=cp.Variable((m,n),pos=True)
y=cp.Variable((m,m),boolean=True)
T=cp.Variable(pos=True)
obj=cp.Minimize(T)
constrains=[]
for i in range(m):
    constrains.append(x[i,2]+t[i][2]<=T)
for i in range(m):
    for j in range(n-1):
        constrains.append(x[i,j]+t[i][j]<=x[i,j+1])
M=800
for i in range(m):
    for k in range(i+1,m):
        for j in range(n):
            constrains.append(x[i,j]+t[i][j]<=x[k,j]+M*(1-y[i,k]))
            constrains.append(x[k,j]+t[k][j]<=x[i,j]+M*y[i,k])
prob=cp.Problem(obj,constrains)
prob.solve(solver='GLPK_MI',verbose=False)
print(int(prob.value),end='')