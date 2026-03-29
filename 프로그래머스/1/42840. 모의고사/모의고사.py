def solution(answers):
    l = len(answers)
    p1 = [i%5+1 for i in range(l)]
    p2 = [2 for i in range(l)]
    p3 = [3 for i in range(l)]
    for i in range(l):
        if i%2==0:
            continue
        else:
            idx = (i//2)%4
            if idx == 0:
                p2[i] = 1
            if idx == 1:
                p2[i] = 3
            if idx == 2:
                p2[i] = 4
            if idx == 3:
                p2[i] = 5
    for i in range(l):
        idx = i % 10
        if idx <= 1:
            continue
        elif idx <= 3:
            p3[i] = 1
        elif idx <= 5:
            p3[i] = 2
        elif idx <= 7:
            p3[i] = 4
        else:
            p3[i] = 5
    
    cnt = [0,0,0]
    for i in range(l):
        if p1[i] == answers[i]:
            cnt[0]+=1
        if p2[i] == answers[i]:
            cnt[1]+=1
        if p3[i] == answers[i]:
            cnt[2]+=1
    max_cnt = max(cnt)
    
    answer = []
    for i in range(3):
        if cnt[i] == max_cnt:
            answer.append(i+1)

    return answer