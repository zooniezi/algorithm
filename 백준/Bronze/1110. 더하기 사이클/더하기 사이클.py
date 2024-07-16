N = int(input())
cycle = 0
tester = N
while True:
    newnum = tester//10 + tester%10
    tester = (tester%10)*10+(newnum%10)
    cycle+=1
    if tester == N:
        print(cycle)
        break