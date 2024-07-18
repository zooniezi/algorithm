import sys
input = sys.stdin.readline

n,m = map(int, input().split())
noHear = {}
noHearSee = []

for i in range(n):
    noHear[input()] = 1

for i in range(m):
    name = input()
    if name in noHear:
        noHear[name] = 0

for key in noHear:
    if noHear[key] == 0:
        noHearSee.append(key)

noHearSee.sort()
print(len(noHearSee))
for name in noHearSee:
    print(name, end="")