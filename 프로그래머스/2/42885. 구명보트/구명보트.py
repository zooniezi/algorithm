from collections import deque

def solution(people, limit):
    people.sort()
    queue = deque(people)
    answer = 0
    temp = limit
    while queue:
        if len(queue) == 1:
            answer+=1
            break
        heavy = queue.pop()
        light = queue.popleft()
        if heavy+light > limit:
            queue.appendleft(light)
            answer+=1
        else:
            answer+=1
    
    return answer
        