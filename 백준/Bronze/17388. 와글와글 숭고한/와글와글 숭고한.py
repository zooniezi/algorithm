nums = list(map(int,input().split()))

sum = nums[0]+nums[1]+nums[2]

if sum >= 100:
    print('OK')
elif nums[0] < nums[1] and nums[0] < nums[2]:
    print('Soongsil')
elif nums[1] < nums[2] and nums[1] < nums[0]:
    print('Korea')
else:
    print("Hanyang")