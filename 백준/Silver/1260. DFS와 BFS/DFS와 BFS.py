import sys
input = sys.stdin.readline

num_of_nodes, num_of_edges, start_node = map(int, input().split())

graph = [[] for i in range(num_of_nodes+1)]

# 그래프 구조 입력받기
for _ in range(num_of_edges):
    start, end = map(int, input().split())
    graph[start].append(end)
    # 간선이 양방향이면 이렇게 기록하는게 이득인가? 결국 방문 노드를 따질때 상관이없나?
    graph[end].append(start)

for each in graph:
    each.sort()


dfs_need_visit, dfs_already_visit = [], []
bfs_need_visit, bfs_already_visit = [], []

#dfs 구현

dfs_need_visit.append(start_node)

while dfs_need_visit:
    now = dfs_need_visit.pop(0)
    
    if now not in dfs_already_visit:
        dfs_already_visit.append(now)

        dfs_need_visit = graph[now] + dfs_need_visit
        
print(*dfs_already_visit)

#bfs 구현

bfs_need_visit.append(start_node)

while bfs_need_visit:
    now = bfs_need_visit.pop(0)

    if now not in bfs_already_visit:
        bfs_already_visit.append(now)

        bfs_need_visit = bfs_need_visit + graph[now]

print(*bfs_already_visit)