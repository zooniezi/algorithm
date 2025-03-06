nums= list(map(int,input().split()))
ans = 0
for i in range(len(nums)):
    ans += 5*nums[i]

print(ans)