from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for now in skill_trees:
        skills = deque(skill)
        temp = True
        for now_skill in now:
            if now_skill in skill:
                check = skills.popleft()
                if check != now_skill:
                    temp = False
                    break
        if temp:
            answer+=1
    return answer