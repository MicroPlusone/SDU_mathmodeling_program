"""
2005B DVD租赁
考虑如下的在线DVD租赁问题。顾客缴纳一定数量的月费成为会员，订购DVD租赁服务。会员对哪些DVD有兴趣，只要在线提交订单，网站就会通过快递的方式尽可能满足要求。会员提交的订单包括多张DVD，这些DVD是基于其偏爱程度排序的。网站会根据手头现有的DVD数量和会员的订单进行分发。每个会员每个月租赁次数不得超过2次，每次获得3张DVD。请考虑以下问题：
数据中会在测试点中给出。数据包括：网站n种DVD的现有张数和当前需要处理的m位会员的在线订单。 如何对这些DVD进行分配，才能使会员获得最大的满意度。
具体数据大家可以参考2005年全国大学生数学建模竞赛B题。
"""
import numpy as np
import cvxpy as cp
m,n=[eval(x) for x in input().split()]
p=np.zeros((m,n))
for i in range(m):
    p[i,:]=[eval(x) for x in input().split()]
d=[eval(x) for x in input().split()]
s=np.zeros((m,n))
for i in range(m):
    for j in range(n):
        if p[i,j]>0:
            s[i,j]=2**(11-p[i,j])
x=cp.Variable((m,n),boolean=True)
obj=cp.Maximize(cp.sum(cp.multiply(s,x)))
cons=[cp.sum(x,axis=0)<=d,cp.sum(x,axis=1)<=3]
prob=cp.Problem(obj,cons)
prob.solve(solver='GLPK_MI')
print(int(prob.value))