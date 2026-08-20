from collections import deque

def solution(queue1, queue2):
    q1_value = sum(queue1)
    q2_value = sum(queue2)
    if (q1_value + q2_value) % 2 == 1:
        return -1

    q1 = deque(queue1)
    q2 = deque(queue2)
    length = len(q1) + len(q2)
    answer = 0

    while q1_value != q2_value:
        if q1_value > q2_value:
            now = q1.popleft()
            q2.append(now)
            q1_value -= now
            q2_value += now
        else:
            now = q2.popleft()
            q1.append(now)
            q2_value -= now
            q1_value += now

        answer += 1
        if answer > length * 2:
            return -1

    return answer