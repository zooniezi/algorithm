import sys

n,money = map(int, input().split())
coin = []
num = 0

for i in range(n):
    coin.append(int(sys.stdin.readline()))

while True:
    now_money = coin.pop()
    if money//now_money == 0:
        continue
    else:
        num += money//now_money
        money = money%now_money
    if money == 0:
        break   

print(num)