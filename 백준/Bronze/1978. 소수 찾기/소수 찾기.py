arr = [1 for i in range(1001)]

arr[0]=-1
arr[1]=-1
for i in range(2,501):
    k = 2
    while True:
        if i*k<=1000:
            arr[i*k]=-1
            k+=1
            continue
        break

primes = []

for i in range(1001):
    if arr[i]==1:
        primes.append(i)

num = int(input())
check_nums = list(map(int, input().split()))
ans = 0
for i in check_nums:
    for prime in primes:
        if prime == i:
            ans +=1
            break
        if prime > i:
            break

print(ans)