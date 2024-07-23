n,m = map(int, input().split())
nums = list(map(int, input().split()))

sums = []
remains = [0 for i in range(m)]
ans = 0

for i in range(n):
    if i == 0:
        sums.append(nums[i]%m)
    else:
        sums.append((sums[i-1]+nums[i])%m)

for i in range(n):
    remains[sums[i]] += 1

for remain in remains:
    if remain != 0:
        ans += ((remain-1)*remain)//2
ans += remains[0]

print(ans)


