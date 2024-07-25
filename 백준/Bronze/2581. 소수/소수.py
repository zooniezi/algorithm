prime = [-1 for i in range(10001)]

for i in range(2,10001):
    if prime[i] == -1:
        prime[i] = 1
        mul = 2
        while True:
            if i*mul>10000:
                break
            prime[i*mul] = 0
            mul+=1

m = int(input())
n = int(input())
sum_of_prime = 0
minimum_prime = 0
for i in range(m,n+1):
    if prime[i] == 1:
        if minimum_prime == 0:
            minimum_prime = i
        sum_of_prime+=i

if minimum_prime == 0:
    print(-1)
else:
    print(sum_of_prime)
    print(minimum_prime)