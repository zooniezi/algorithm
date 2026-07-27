def solution(k, ranges):
    collatz = []
    while k!=1:
        collatz.append(k)
        if k%2==0:
            k = k//2
        else:
            k = k*3 + 1
        if k == 1:
            collatz.append(k)
    l = len(collatz)-1
    answer = []
    
    for now in ranges:
        ans = 0
        start = now[0]
        end = now[1]
        if l+end < start:
            answer.append(-1)
        else:
            if start == l:
                answer.append(0)
                continue
            for i in range(start,l+end):
                ans+=(collatz[i]+collatz[i+1])/2
            answer.append(ans)
    
    return answer