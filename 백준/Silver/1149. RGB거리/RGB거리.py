import sys
n = int(input())
dp = [[0 for color in range(3)] for i in range(n+1)]

for i in range(1,n+1):
    r,g,b = map(int, sys.stdin.readline()[:-1].split())
    if i == 1:
        dp[1][0] = r
        dp[1][1] = g
        dp[1][2] = b
        continue
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + r
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + g
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + b
print(min(dp[n]))    
        
