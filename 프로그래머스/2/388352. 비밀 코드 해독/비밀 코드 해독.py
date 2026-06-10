from itertools import combinations

def solution(n, q, ans):
    answer = 0
    nums = [i for i in range(1,n+1)]
    check_list = list(combinations(nums,5))
    m = len(q)
    for now in check_list:
        is_ans = True
        for i in range(m):
            cnt = 0
            for j in range(5):
                if now[j] in q[i]:
                    cnt += 1
            if cnt != ans[i]:
                is_ans = False
                break
        if is_ans:
            answer+=1
            
    
    return answer