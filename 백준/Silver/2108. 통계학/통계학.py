import sys
n = int(input())
arr = []
check = [0 for i in range(8001)]
for i in range(n):
    now = int(sys.stdin.readline())
    arr.append(now)
    check[now] += 1

#평균
average = 0
for i in range(n):
    average+=arr[i]
average = round(average/n)
print(average)

# 중앙값
arr.sort()
print(arr[(n-1)//2])

# 최빈값
max_indexes = []
for i in range(8001):
    if i == 0:
        max_indexes.append(i)
        continue
    if check[i] > check[max_indexes[0]]:
        max_indexes = []
        max_indexes.append(i)
    elif check[i] == check[max_indexes[0]]:
        max_indexes.append(i)

for i in range(len(max_indexes)):
    if max_indexes[i] > 4000:
        max_indexes[i] -= 8001

max_indexes.sort()

if len(max_indexes) == 1:
    print(max_indexes[0])
else:
    print(max_indexes[1])


# 범위
print(arr[-1]-arr[0])