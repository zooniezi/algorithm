N = int(input())
M = int(input())
S = input()
cnt = 0
for i in range(M):
    if S[i] == "I":
        ioi = True
        if i+(2*N)<M:
            for j in range(1,(N*2)+1):
                if S[i+j] == S[i+j-1]:
                    ioi = False
                    break
            if ioi:
                cnt +=1
print(cnt)