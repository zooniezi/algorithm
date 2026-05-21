from collections import deque

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    result = [0 for i in range(m+1)]
    visited = [[0 for i in range(m)] for j in range(n)]
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                count = 0 
                visited[i][j] = 1
                queue = deque()
                queue.append([i,j])
                miny, maxy = j,j
                while queue:
                    x,y = queue.popleft()
                    miny = min(miny,y)
                    maxy = max(maxy,y)
                    count += 1
                    for t in range(4):
                        nowx = x+dx[t]
                        nowy = y+dy[t]
                        if nowx < 0 or nowx >= n or nowy < 0 or nowy >= m:
                            continue
                        if visited[nowx][nowy] == 0 and land[nowx][nowy] == 1:
                            visited[nowx][nowy] = 1
                            queue.append([nowx,nowy])
                for k in range(miny, maxy+1):
                    result[k] += count
    answer = max(result)
    return answer