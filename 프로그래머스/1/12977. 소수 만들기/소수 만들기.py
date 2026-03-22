def solution(nums):
    answer = 0
    test = 0
    for i in range(len(nums)-2):
        test += nums[i]
        for j in range(i+1,len(nums)-1):
            test += nums[j]
            for k in range(j+1, len(nums)):
                test += nums[k]
                temp = False
                for div in range(2,int(test**0.5)+1):
                    if test%div == 0:
                        temp = True
                        break
                if not temp:
                    answer+=1
                test -= nums[k]
            test -= nums[j]
        test -= nums[i]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer