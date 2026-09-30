def solution(n):
    temp = []
    while n:
        t = n%3
        if t==0:
            t = 4
            n -= 1
        temp.append(str(t))
        n//=3
    print(temp)
    temp.reverse()
    print(temp)
    answer = ''.join(temp)
    return answer