primes = [0 for i in range(1000001)]
primes[0] = 1
primes[1] = 1
check = 0
for i in range(2, 1001):
    if primes[i] == 0:
        check +=1
        cnt = 2
        while True:
            if i*cnt <= 1000000:
                primes[i*cnt] = 1
                cnt += 1
                continue
            break


a, b = map(int, input().split())

for i in range(a,b+1):
    if primes[i]==0:
        print(i)