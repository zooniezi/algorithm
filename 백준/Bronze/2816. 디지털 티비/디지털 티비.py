n = int(input())
kbs1 = 0
kbs2 = 0
for i in range(n):
    channel = input()
    if channel == 'KBS1':
        kbs1 = i
    if channel == 'KBS2':
        kbs2 = i

ans = ''

if kbs1 > kbs2:
    kbs2+=1

for i in range(kbs1):
    ans = ans + '1'

for i in range(kbs1):
    ans = ans + '4'

for i in range(kbs2):
    ans = ans + '1'

for i in range(kbs2-1):
    ans = ans + '4'

print(ans)
