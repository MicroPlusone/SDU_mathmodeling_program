"""
已知某种商品m个仓库的存货量，n个客户对该商品的需求量，单位商品运价。试确定m个仓库到n个客户的商品调运数量，使总的运输费用最小。
"""
import cvxpy as cp
import numpy as np
m,n = [eval(x) for x in input().split()]
c=np.zeros((m,n))
for i in range(m):
    c[i,:]=[eval(x) for x in input().split()]
d=[eval(x) for x in input().split()]
e=[eval(x) for x in input().split()]
x=cp.Variable((m,n))
obj=cp.Minimize(cp.sum(cp.multiply(c,x)))
con1=cp.sum(x,axis=1)<=e
con2=cp.sum(x,axis=0)==d
con3=x>=0
cons=[con1,con2,con3]
prob=cp.Problem(obj,cons)
prob.solve()
print("{0:.2f}".format(prob.value),end='')