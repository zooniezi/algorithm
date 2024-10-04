import sys
input = sys.stdin.readline
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = triangle[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + triangle[i][0]
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]
if n >=2:
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    result = max(dp[n-1])
    print(result)
else:
    result = max(dp[n-1])
    print(result)