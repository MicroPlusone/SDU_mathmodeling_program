"""
给定两个大小相同方阵，将经典矩阵乘积运算修改：将原来的元素之间的乘法改为加法，将原来的加法改为取小。
设A=(ai,j)n×n,B=(bi,j)n×n，新运算的结果为C=(ci,j) n×n，则ci,j= min{ai,k+bk,j,k=1,⋯,n}

输入格式:
第一行输入一个整数n，表示方阵的大小。
第二行到2n+1行，每一行数据有n个，空格隔开。
第二行行到n+1行是矩阵A的元素。
最后n行是矩阵B的元素。

说明：n不超过100，矩阵所有元素都是整数。


"""

def new_mutiple(A,B,n):
    C=[]
    for i in range(n):
        c=[]
        for j in range(n):
            c1=[]
            for k in range(n):
                c1.append(A[i][k]+B[k][j])
            c.append(min(c1))
        C.append(c)
    return C

n=int(input())
m=[]
for i in range(2):
    m1=[]
    for j in range(n):
        m2=input()
        m2=[eval(i) for i in m2.split(' ')]
        m1.append(m2)
    m.append(m1)

A=m[0]
B=m[1]
C=new_mutiple(A,B,n)
for row in C[0:n-1]:
    for j in range(len(row)-1):
        print(row[j],end=' ')
    print(row[-1])
for i in range(len(C[-1])-1):
    print(C[-1][i],end=' ')
print(C[-1][-1],end='')
exit(0)
