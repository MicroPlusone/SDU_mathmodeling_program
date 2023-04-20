"""
假设你正在规划一次城市间的旅行。城市之间由双向道路连接。每条道路都有一个距离，表示行驶这条道路所需的时间。你的任务是找到从起始城市到目标城市的最短时间路径。 请你编写一个程序，根据输入的城市和道路信息，输出从起始城市到目标城市的最短时间。
输入格式:
第1行包含3个整数：n表示城市数量，m表示道路数量，k表示查询数量。
接下来m行，每行包含3个整数：a, b, t，表示城市a和城市b之间有一条双向道路，行驶这条道路需要t时间。城市的编号从1到n。
接下来k行，每行包含2个整数：s, d，表示一次查询，从城市s出发到达城市d。
输出格式：
输出k行，每行包含一个整数，表示对应查询的最短时间。
如果无法到达目标城市，输出-1。
"""
import networkx as nx
def shortest_path_networkx(n,edges,queries):
    G=nx.Graph()
    G.add_nodes_from(range(1,n+1))
    G.add_weighted_edges_from(edges)
    results=[]
    for s,d in queries:
        try:
            path_length=nx.dijkstra_path_length(G,s,d,weight='weight')
            results.append(path_length)
        except nx.NetworkXNoPath:
            results.append(-1)
    return results
n,m,k=[eval(x) for x in input().split()]
edges=[]
for i in range(m):
    edges.append(tuple(map(int,input().split())))
queries=[]
for i in range(k):
    queries.append(tuple(map(int,input().split())))
result = shortest_path_networkx(n,edges,queries)
for r in result:
    print(r)