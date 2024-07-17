arr = [0 for i in range(1000001)]

def maker(num):
    total = 0
    while True:
        if num == 0:
            return total
        total+=num%10
        num = num//10

for i in range(1,1000001):
    check = maker(i)+i
    if check <= 1000000:
        if arr[check] == 0:
            arr[check]=i

print(arr[int(input())])