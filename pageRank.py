from collections import Counter

import networkx as nx
import scipy as sp
from time import time

begin = time()
data = open('data/fb-pages-government.edges')


N = len(data.readlines())
data = open('data/fb-pages-government.edges')

out_degree = {}
in_degree = {}

# info1 = data.readline()
# info2 = data.readline()
# info3 = data.readline()
# info4 = data.readline()

G = nx.Graph()
cnt = 0
for line in data:
    if cnt == N + 1:
        break
    from_ID, to_ID = map(int, line.split(","))
    G.add_edge(from_ID, to_ID)
    cnt += 1

    # 计数出度和入度
    if from_ID in out_degree:
        out_degree[from_ID] = out_degree[from_ID] + 1
    else:
        out_degree[from_ID] = 1
    if from_ID not in in_degree:
        in_degree[from_ID] = 0

    if to_ID in in_degree:
        in_degree[to_ID] = in_degree[to_ID] + 1
    else:
        in_degree[to_ID] = 1
    if to_ID not in out_degree:
        out_degree[to_ID] = 0

print(G.number_of_edges())
print(G.number_of_nodes())

DictPage = nx.pagerank(G)

# 排序从大到小
c = Counter(DictPage).most_common()

end = time()

with open('output/fb-pages-government_PageRank_result.csv', 'w+') as f:
    f.write('Ranking,UserID,PageValue,OutDegree,InDegree\n')
    rank = 1
    for node in c:
        f.write('%d,%d,%1.3e,%d,%d\n' % (rank, node[0], node[1], out_degree.get(node[0]), in_degree.get(node[0])))
        rank += 1

print(len(DictPage))
print("时长:%f" % (end - begin))
