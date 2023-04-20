"""
某国家有n个城市，编号为1到n。为了促进城市间的发展，政府决定建设一个高速网络连接各个城市。每个城市之间有一些现有的道路可以升级为高速网络，但升级的成本各不相同。政府希望以最低的成本连接所有城市，同时确保网络中任意两个城市之间都有直接或间接的高速连接。
给定一个城市之间现有道路的升级成本，你需要找出连接所有城市的最低成本。
输入格式:
第1行包含2个整数：n表示城市数量，m表示现有道路数量。
接下来m行，每行包含3个整数：a, b, c，表示城市a和城市b之间有一条现有道路，升级成本为c。城市的编号从1到n。
输出格式:
输出一个整数，表示连接所有城市的最低成本。
"""
import networkx as nx
def minimum_cost_network(n,roads):
    G=nx.Graph()
    G.add_nodes_from(range(1,n+1))
    G.add_weighted_edges_from(roads)
    min_tree=nx.minimum_spanning_tree(G)
    min_cost=sum(data['weight'] for u,v,data in min_tree.edges(data=True))
    return min_cost
n,m=map(int,input().strip().split())
roads=[]
for _ in range(m):
    a,b,c=map(int,input().strip().split())
    roads.append((a,b,c))
result=minimum_cost_network(n,roads)
print(result)