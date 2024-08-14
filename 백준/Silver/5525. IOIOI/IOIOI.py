N = int(input())
M = int(input())
S = input()
cnt = 0
i = 0
ans = 0
while i < M:
    if S[i:i+3] == "IOI":
        i+=2
        cnt += 1
        if cnt == N:
            ans+=1
            cnt-=1
    else:
        i+=1
        cnt = 0
        
print(ans)