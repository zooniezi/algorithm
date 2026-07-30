def solution(order):
    length = len(order)
    target_box = 1
    stack = []
    
    answer = 0
    for box in order:
        while target_box < box:
            stack.append(target_box)
            target_box += 1
        
        if target_box == box:
            answer += 1
            target_box += 1
            continue
        
        if stack.pop() == box:
            answer += 1
            continue
        
        break
    
    return answer