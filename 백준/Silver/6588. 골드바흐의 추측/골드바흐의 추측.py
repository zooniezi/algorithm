import sys

check = [0 for i in range(1000001)]
check[0] = 1
check[1] = 1
prime = []
for i in range(2,1001):
    if check[i] == 0:
        temp = 2
        while i*temp <=1000000:
            check[i*temp] = 1
            temp += 1

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3,1000001,2):
        if check[i] == 0 and check[n-i] == 0:
            print(f'{n} = {i} + {n-i}')
            break