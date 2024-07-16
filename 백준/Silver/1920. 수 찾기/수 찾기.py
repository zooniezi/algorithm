num = int(input())
nums = list(map(int, input().split()))
num2 = int(input())
check_nums = list(map(int, input().split()))

nums.sort()

def binary_search(wanna_check, start_index, end_index, data):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2

    if wanna_check == data[mid_index]:
        return mid_index
    
    if wanna_check < data[mid_index]:
        return binary_search(wanna_check, start_index, mid_index-1, data)
    
    return binary_search(wanna_check, mid_index+1, end_index, data)


for i in range(num2):
    check = binary_search(check_nums[i], 0, num-1, nums)
    if check == -1:
        print(0)
    else:
        print(1)    


