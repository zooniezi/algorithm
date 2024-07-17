import sys

n = int(input())
if n == 0:
    print(0)
else:
    nums = [int(sys.stdin.readline()) for i in range(n)]

    nums.sort()
    cut_num = int(n*0.15+0.5)

    final_num = nums[cut_num:n-cut_num]
    t = 0
    for i in final_num:
        t+=i

    ans = t/(len(final_num))
    print(int(ans+0.5))
