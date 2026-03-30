from collections import deque

def solution(progresses, speeds):
    queue = deque()
    for i in range(len(progresses)):
        work = [progresses[i], speeds[i]]
        queue.append(work)
    answer = []
    while True:
        if not queue:
            break
        cnt = 0
        for each in queue:
            each[0] += each[1]
        while queue:
            if queue[0][0] >= 100:
                queue.popleft()
                cnt+=1
            else:
                break
        if cnt!=0:
            answer.append(cnt)

    return answer