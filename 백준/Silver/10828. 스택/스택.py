import sys

def push(list, N):
    list.append(N)

def pop(list):
    if not len(list) == 0:
        print(list[-1])
        del list[-1]
        return 0
    print(-1)
    return 0

def size(list):
    print(len(list))
    return 0

def empty(list):
    if len(list) == 0:
        print(1)
        return 0
    print(0)
    return 0

def top(list):
    if not len(list) == 0:
        print(list[-1])
        return 0
    print(-1)
    return 0

n = int(input())
stack = []
while True:
    try:
        input = sys.stdin.readline()
        input = input[:-1]
        command = list(map(str, input.split()))

        if command[0] == 'push':
            push(stack, int(command[1]))
        if command[0] == 'pop':
            pop(stack)
        if command[0] == 'size':
            size(stack)
        if command[0] == 'empty':
            empty(stack)
        if command[0] == 'top':
            top(stack)
    except:
        break