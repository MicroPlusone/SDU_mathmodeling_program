"""
某农村地区有n个农田，编号为1到n。为了灌溉这些农田，政府决定在农田之间修建一个供水系统。这个供水系统由若干条有向水管组成，每条水管连接两个农田，并具有一定的流量限制。
给定这些农田之间的水管及其流量限制，请确定在确保供水系统中无水回流的情况下，从1号农田到n号农田的最大流量是多少。
输入格式:
第1行包含2个整数：n表示农田数量，m表示水管数量。
接下来m行，每行包含3个整数：a, b, c，表示从农田a到农田b有一条有向水管，其流量限制为c。农田的编号从1到n。
输出格式:
输出一个整数，表示从1号农田到n号农田的最大流量。
"""
import networkx as nx
def max_flow(n,pipes):
    G=nx.DiGraph()
    G.add_nodes_from(range(1,n+1))
    for a,b,c in pipes:
        G.add_edge(a,b,capacity=c)
    flow_value, flow_dict=nx.maximum_flow(G,1,n)
    return flow_value
n,m=map(int,input().strip().split())
pipes=[]
for _ in range(m):
    a,b,c=map(int, input().strip().split())
    pipes.append((a,b,c))
result=max_flow(n,pipes)
print(result)