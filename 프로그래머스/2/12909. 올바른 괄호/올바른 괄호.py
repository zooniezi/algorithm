from collections import deque

def solution(s):
    answer = True
    depth = 0
    for i in s:
        if i == "(":
            depth+=1
        else:
            depth-=1
        
        if depth < 0:
            return False
    
    if depth == 0:
        return True
    else:
        return False