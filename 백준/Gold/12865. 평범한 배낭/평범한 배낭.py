n,k = map(int,input().split())

bags = []
dp = [0 for i in range(k+1)]

for i in range(n):
    weight, value = map(int,input().split())
    bags.append([weight,value])

for each_bag in bags:
    now_w = each_bag[0]
    now_v = each_bag[1]

    for i in range(k,now_w-1,-1):
        dp[i] = max(dp[i],dp[i-now_w]+now_v)

print(dp[k])
        
