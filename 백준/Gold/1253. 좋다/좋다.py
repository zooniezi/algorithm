n = int(input())

nums = list(map(int, input().split()))

nums.sort()
cnt = 0
for i in range(n):
    check = nums[i]
    temp = nums.copy()
    del temp[i]
    good = 0
    start = 0
    end = len(temp)-1

    while True:
        if start == end:
            good = 0
            break
        if temp[start] + temp[end] == check:
            good = 1
            break
        elif temp[start] + temp[end] > check:
            end -= 1
        elif temp[start] + temp[end] < check:
            start += 1
    
    if good == 1:
        cnt += 1
        good = 0

print(cnt)