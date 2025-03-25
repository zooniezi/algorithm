import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = input().rstrip()
lenbomb = len(bomb)
stack = []

for letter in word:
    stack.append(letter)
    if len(stack) < lenbomb:
        continue
    
    isExplode = True
    if ''.join(stack[-lenbomb:]) != bomb:
        isExplode = False
    
    if isExplode:
        for i in range(lenbomb):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))