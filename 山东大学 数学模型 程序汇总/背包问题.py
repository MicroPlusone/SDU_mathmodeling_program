"""
假设你是一名登山者，你要爬上一座高峰。你必须携带足够的衣物、食物、水源和其他必需品来保持你在漫长的旅途中的安全和健康。 然而，由于你需要攀登峰顶，你只能携带有限的重量。例如，你可以携带一个重量为50磅的背包，并且你必须6个物品中选择，这些物品的重量是
10, 20, 30, 40, 50, 60
对应的价值是：
7, 8, 10, 4, 5, 6
你必须选择哪些物品携带到山顶，并且使它们的总重量不超过50磅，使得总的价值最大。
这个问题就是一个经典的 0-1 背包问题，可以使用整数规划等方法来解决。
该问题的数学模型如下
n 个物品，分别是 1,2,...,n。
wi表示第 i 个物品的重量，i∈1,2,...,n。
vi表示第 i 个物品的价值（或重要性），i∈1,2,...,n。
W 是背包的最大容量。
定义一个 0-1 的决策变量 xi，表示我们是否选择包含第 i 个物品：
xi=1 if item i is selected,
xi=0 if item i is not selected,
我们的目标是选择一个组合，以最大化包含的物品的总价值，并且仍然满足背包的容量限制，即：
max∑i=1n​vixisubject to:∑i=1nwixi≤W, and xi∈0,1 for all i∈1,2,...,n
输入格式:
第1行输入两个数，n表示物品数量，W表示背包最大承受重量
第2行n个数表示物品的重量
第3行n个数表示物品的价值
输出格式:
背包所装物品的最大价值，最终结果为整数。
"""
import cvxpy as cp
n,W =[eval(x) for x in input().split(',')]
weights=[eval(x) for x in input().split(',')]
values=[eval(x) for x in input().split(',')]
x=cp.Variable(n,boolean=True)
objective=cp.Maximize(cp.sum(cp.multiply(x,values)))
constraints=[cp.sum(cp.multiply(x,weights))<=W]
problem=cp.Problem(objective,constraints)
problem.solve()
print(int(objective.value),end='')