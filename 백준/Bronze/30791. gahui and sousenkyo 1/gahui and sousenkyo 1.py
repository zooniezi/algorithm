a = list(map(int,input().split()))
cnt = 0
for i in range(1,5):
    if a[0]-a[i]<=1000:
        cnt+=1
print(cnt)