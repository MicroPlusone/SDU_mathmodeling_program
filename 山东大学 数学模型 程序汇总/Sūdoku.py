a=[[0]*10 for i in range(10)]
h=[[True]*10 for i in range(10)]
l=[[True]*10 for i in range(10)]
g=[[True]*10 for i in range(10)]
def print_board():
    for i in range(1,10):
        for j in range(1,10):
            print(a[i][j],end=' ')
        if i != 9:
            print()
    exit(0)
def dfs(x,y):
    if a[x][y]!=0:
        if x==9 and y==9:
            print_board()
        if y==9:
            dfs(x+1,1)
        else:
            dfs(x,y+1)
    if a[x][y]==0:
        for i in range(1,10):
            if h[x][i] and l[y][i] and g[(x-1)//3*3+(y-1)//3+1][i]:
                a[x][y]=i
                h[x][i]=False
                l[y][i]=False
                g[(x-1)//3*3+(y-1)//3+1][i]=False
                if x==9 and y==9:
                    print_board()
                if y==9:
                    dfs(x+1,1)
                else:
                    dfs(x,y+1)
                a[x][y]=0
                h[x][i]=True
                l[y][i]=True
                g[(x-1)//3*3+(y-1)//3+1][i]=True
def main():
    for i in range(1,10):
        row=list(map(int,input().split()))
        for j in range(1,10):
            a[i][j]=row[j-1]
            if a[i][j]>0:
                h[i][a[i][j]]=False
                l[j][a[i][j]]=False
                g[(i-1)//3*3+(j-1)//3+1][a[i][j]]=False
    dfs(1,1)
main()
