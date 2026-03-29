def solution(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1
    l = len(list(dict.keys()))
    if l <= len(nums)//2:
        return l
    else:
        return len(nums)//2
