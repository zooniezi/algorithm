def solution(storage, requests):
    answer = 0
    n = len(storage)
    m = len(storage[0])
    is_cargo = [[0 for i in range(m+2)] for j in range(n+2)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            is_cargo[i][j] = 1
    
    
    
    for req in requests:
        
        cargo_outside = set()
    
        stack = [(0,0)]
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        is_visited = [[0 for i in range(m+2)] for j in range(n+2)]
        is_visited[0][0] = 1
        while stack:
            now = stack.pop()
            for d in range(4):
                if now[0]+dx[d]>=0 and now[0]+dx[d]<n+2 and now[1]+dy[d]>=0 and now[1]+dy[d]<m+2:
                    if is_visited[now[0]+dx[d]][now[1]+dy[d]] == 0:
                        if is_cargo[now[0]+dx[d]][now[1]+dy[d]] == 0:
                            stack.append((now[0]+dx[d],now[1]+dy[d]))
                            is_visited[now[0]+dx[d]][now[1]+dy[d]] = 1
                        else:
                            cargo_outside.add((now[0]+dx[d],now[1]+dy[d]))
        
        if len(req) == 1:
            for each in cargo_outside:
                if storage[each[0]-1][each[1]-1] == req:
                    is_cargo[each[0]][each[1]] = 0
        
        if len(req) == 2:
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == req[0]:
                        is_cargo[i+1][j+1] = 0
            
    for i in range(n+2):
        for j in range(m+2):
            if is_cargo[i][j] == 1:
                answer +=1
    
    return answer