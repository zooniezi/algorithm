import sys
input = sys.stdin.readline

prime = [1 for i in range(246913)]
prime[0] = 0
prime[1] = 0

#make prime list
for i in range(2,498):
    if prime[i] == 1:
        temp = 2*i
        while temp <= 246912:
            prime[temp] = 0
            temp += i

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in range(n+1,2*n+1):
        if prime[i] == 1:
            cnt += 1
    print(cnt)