sums = [0 for i in range(1001)]

cnt = 1
now_num = 1
for i in range(1,1001):
    cnt-=1
    sums[i]=sums[i-1]+now_num

    if cnt==0:
        now_num+=1
        cnt=now_num

a,b = map(int,input().split())

print(sums[b]-sums[a-1])