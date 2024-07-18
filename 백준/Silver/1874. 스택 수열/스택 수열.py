n = int(input())
arr = []
stack = []
possible = True

check = 1

for i in range(n):
    now_num = int(input())
    while check <= now_num:
        arr.append('+')
        stack.append(check)
        check += 1
    
    if stack[-1] == now_num:
        stack.pop()
        arr.append('-')
    else:
        possible = False

if not possible:
    print('NO')
else:
    for i in arr:
        print(i)