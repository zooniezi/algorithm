import sys

check = [0 for i in range(10001)]

n = int(input())

for i in range(n):
    check[int(sys.stdin.readline())] += 1

for i in range(1,10001):
    for j in range(check[i]):
        print(i)