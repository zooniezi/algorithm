testcase = int(input())
dp = [[0 for i in range(41)] for i in range(41)]
dp[0] = [0,1]
dp[1] = [1,0]
for i in range(2,41,1):
    dp[i][0]=dp[i-1][0]+dp[i-2][0]
    dp[i][1]=dp[i-1][1]+dp[i-2][1]
for i in range(testcase):
    n = int(input())
    print(dp[n][1], dp[n][0])
    #아놔 자리 바꿔서 코드 썻네;;