from collections import deque

def solution(x, y, n):
    queue = deque([(x,0)])
    visited = [0 for i in range(1000001)]
    answer = -1
    
    while queue:
        now = queue.popleft()
        now_num = now[0]
        now_ans = now[1]
        if now_num == y:
            answer = now_ans
            break
        else:
            if now_num+n <= y and visited[now_num+n] == 0:
                queue.append((now_num+n,now_ans+1))
                visited[now_num+n] = 1
            if now_num*2 <= y and visited[now_num*2] == 0:
                queue.append((now_num*2,now_ans+1))
                visited[now_num*2] = 1
            if now_num*3 <= y and visited[now_num*3] == 0:
                queue.append((now_num*3,now_ans+1))
                visited[now_num*3] = 1
    return answer