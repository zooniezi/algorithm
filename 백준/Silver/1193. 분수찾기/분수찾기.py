n = int(input())

cnt = 1
remain = 0
while True:
    if n-cnt <= 0:
        remain = n
        break
    else:
        n -= cnt
        cnt += 1

if cnt%2 == 0:
    print(remain,"/",cnt-remain+1, sep="")
else:
    print(cnt-remain+1, "/", remain, sep="")
