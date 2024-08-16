from collections import deque

n,m = map(int, input().split())

campus = []
for _ in range(n):
    campus.append(list(map(str,input())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

friends = 0

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            search = deque([[i,j]])
            while search:
                now = search.popleft()
                for d in range(4):
                    if 0<= now[0]+dx[d] < n and 0<=now[1]+dy[d]<m:
                        if campus[now[0]+dx[d]][now[1]+dy[d]] != 'X':
                            if campus[now[0]+dx[d]][now[1]+dy[d]] == 'P':
                                friends += 1
                            campus[now[0]+dx[d]][now[1]+dy[d]] = 'X'
                            search.append([now[0]+dx[d],now[1]+dy[d]])

if friends != 0:
    print(friends)
else:
    print('TT')