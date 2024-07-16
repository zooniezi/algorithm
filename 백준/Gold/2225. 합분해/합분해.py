summer = [[0 for i in range(201)]for i in range(201)]
n,k= map(int,input().split())
for i in range(201):
    summer[i][1]=1
    summer[i][2]=i+1
for i in range(201):
    summer[1][i]=i
    for j in range(2,201,1):
        summer[j][i]=(summer[j-1][i]+summer[j][i-1])%1000000000

print(summer[n][k])