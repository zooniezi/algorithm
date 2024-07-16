n = int(input())
num = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))


ans = [0]*20000001

for i in num:
    ans[i]+=1

for i in check:
    print(ans[i], end=" ")