def solution(clothes):
    dict = {}
    for each in clothes:
        if each[1] in dict:
            dict[each[1]] += 1
        else:
            dict[each[1]] = 1
    
    answer = 1
    for each in dict:
        answer *= (dict[each])+1
    answer -=1
    
    return answer