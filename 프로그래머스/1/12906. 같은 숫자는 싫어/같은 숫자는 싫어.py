from collections import deque

def solution(arr):
    answer = deque([])
    for num in arr:
        if not answer:
            answer.append(num)
        if num!=answer[-1]:
            answer.append(num)
    answer_list = list(answer)
    return answer_list