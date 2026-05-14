def solution(topping):
    answer = 0

    cake1 = {}
    cake2 = {}
    
    for t in topping:
        if t in cake1:
            cake1[t] += 1
        else:
            cake1[t] = 1
    
    for t in topping:
        if len(cake1) == len(cake2):
            answer += 1
        cake1[t] -= 1
        if cake1[t] == 0:
            del cake1[t]
        if t in cake2:
            cake2[t] += 1
        else:
            cake2[t] = 1
        
    return answer