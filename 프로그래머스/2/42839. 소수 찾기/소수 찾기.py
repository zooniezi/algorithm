from itertools import permutations

def solution(numbers):
    temp = []
    for i in numbers:
        temp.append(i)
        
    cnt = 0
    candidates = set()
    
    for permute_num in range(1,len(temp)+1):
        
        nums = set(list(permutations(temp,permute_num)))
        candidate = list(nums)
        for i in candidate:
            candidates.add(int("".join(i)))
    
    for i in candidates:
        if i <= 1:
            continue
        check = True
        
        for div in range(2,int(i**0.5)+1):
            if i%div == 0:
                check = False
                break
        if check:
            cnt += 1
    return cnt