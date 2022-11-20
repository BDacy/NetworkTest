import networkx as nx
from time import time


begin = time()
data = open('data/fb-pages-government.edges')

N = 89455

out_degree = {}
in_degree = {}

info1 = data.readline()
info2 = data.readline()
info3 = data.readline()
info4 = data.readline()

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

listVote = nx.voterank(G)
end = time()

with open('output/fb-pages-government_VoteRank_result.csv', 'w+') as f:
    f.write('Ranking,UserID,OutDegree,InDegree\n')
    rank = 1
    for node in listVote:
        f.write('%d,%d,%d,%d\n' % (rank, node, out_degree.get(node), in_degree.get(node)))
        rank += 1

print(len(listVote))
print("时长:%f" % (end - begin))
