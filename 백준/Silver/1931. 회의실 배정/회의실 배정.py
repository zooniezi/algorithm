import sys
input = sys.stdin.readline

n = int(input())

times = []

for i in range(n):
    time = list(map(int,input().split()))
    times.append(time)

times.sort(key= lambda x : (x[1],x[0]))
ans = []
ans.append(times.pop(0))

for i in range(n-1):
    if times[i][0] >= ans[-1][1]:
        # if ans[-1][0] != ans[-1][1] or times[i][0]!=times[i][1]:
        ans.append(times[i])

print(len(ans))