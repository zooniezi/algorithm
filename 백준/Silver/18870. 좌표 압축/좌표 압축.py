n = int(input())
nums = list(map(int, input().split()))

check = [0]*n

sort_nums = sorted(list(set(nums)))
dict_nums = dict(zip(sort_nums, list(range(len(sort_nums)))))


for i in range(n):
    print(dict_nums[nums[i]],end=" ")