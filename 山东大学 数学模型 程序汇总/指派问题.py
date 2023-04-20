"""
5个人从事5项工作的绩效如下
100,0,100,267,100
400,200,100,153,33
200,800,100,99,33
200,0,100,451,34
100,0,600,30,800
每个人需要完成一个工作，每个工作只能安排一个人。如何安排工作，使得总体绩效达到最大？
"""
import cvxpy as cp
import numpy as np
n=eval(input())
c=np.zeros((n,n))
for i in range(n):
    c[i,:]=[eval(x) for x in input().split(',')]
x=cp.Variable((n,n),boolean=True)
objective=cp.Maximize(cp.sum(cp.multiply(c,x)))
constraints=[
    cp.sum(x,axis=0)==np.ones(n),
    cp.sum(x,axis=1)==np.ones(n)
]
problem=cp.Problem(objective,constraints)
problem.solve()
print("{0:.2f}".format(problem.value),end="")