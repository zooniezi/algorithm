from collections import deque

def solution(expression):
    nums = deque([])
    operation = deque([])
    temp = ''
    for ch in expression:
        if ch in '+-*':
            operation.append(ch)
            nums.append(int(temp))
            temp = ''
        else:
            temp += ch
    nums.append(int(temp))

    possible = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','+','-'],['*','-','+']]
    answer = 0

    for order in possible:
        cur_nums = deque(nums)
        cur_ops = deque(operation)

        for each in order:
            new_nums = deque([cur_nums.popleft()])
            new_ops = deque()

            while cur_ops:
                now_op = cur_ops.popleft()
                b = cur_nums.popleft()

                if now_op == each:
                    a = new_nums.pop()
                    if each == '+':
                        new_nums.append(a + b)
                    elif each == '-':
                        new_nums.append(a - b)
                    else:
                        new_nums.append(a * b)
                else:
                    new_nums.append(b)
                    new_ops.append(now_op)

            cur_nums, cur_ops = new_nums, new_ops

        answer = max(answer, abs(cur_nums[0]))

    return answer