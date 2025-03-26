import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
lab = [list(map(int,input().split())) for i in range(n)]
empty_space = []
empty_count = 0
virus_space = []
virus_cnt = 0
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty_space.append([i,j])
            empty_count+=1
        if lab[i][j] == 2:
            virus_space.append([i,j])
            virus_cnt += 1

test = list(combinations(empty_space,3))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0

for now_test in test:
    for i in now_test:
        lab[i[0]][i[1]] = 1
    
    visited = [[0 for i in range(m)] for j in range(n)]
    visited_cnt = 0
    spread_virus = deque(virus_space)
    while spread_virus:
        now = spread_virus.popleft()
        if visited[now[0]][now[1]] == 1:
            continue
        visited[now[0]][now[1]] = 1
        visited_cnt += 1
        for d in range(4):
            x = dx[d]
            y = dy[d]
            if now[0]+x >= 0 and now[0]+x<n and now[1]+y>=0 and now[1]+y<m:
                if visited[now[0]+x][now[1]+y] == 1:
                    continue
                else:
                    if lab[now[0]+x][now[1]+y] == 0:
                        spread_virus.append([now[0]+x,now[1]+y])

    
    ans = max(ans, (empty_count-3)-(visited_cnt-virus_cnt))
    for i in now_test:
        lab[i[0]][i[1]] = 0

print(ans)
