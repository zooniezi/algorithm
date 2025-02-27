import sys

input = sys.stdin.readline

n,m = map(int, input().split())


candy = [[0 for i in range(301)] for j in range(301)]
dp = [[0 for i in range(301)] for j in range(301)]
ans = 0

for i in range(n):
    x,y = map(int,input().split())
    candy[x][y] = m

for i in range(301):
    for j in range(301):
        now_candy = max(0,candy[i][j]-(i+j))
        if i==0 and j==0:
            dp[i][j] = now_candy
        elif i > 0 and j > 0:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + now_candy
        elif i==0:
            dp[i][j] = dp[i][j-1] + now_candy
        else:
            dp[i][j] = dp[i-1][j] + now_candy
    
        ans = max(ans,dp[i][j])

print(ans)