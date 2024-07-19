import sys
deque = []

def push_front(x):
    global deque
    deque = [x] + deque
    return

def push_back(x):
    global deque
    deque.append(x)
    return

def pop_front():
    global deque
    if len(deque) == 0:
        print(-1)
        return
    print(deque[0])
    del deque[0]
    return

def pop_back():
    global deque
    if len(deque) == 0:
        print(-1)
        return
    print(deque[-1])
    del deque[-1]
    return

def size():
    global deque
    print(len(deque))
    return

def empty():
    global deque
    if len(deque) == 0:
        print(1)
        return
    print(0)
    return

def front():
    global deque
    if len(deque) == 0:
        print(-1)
        return
    print(deque[0])
    return

def back():
    global deque
    if len(deque) == 0:
        print(-1)
        return
    print(deque[-1])
    return

n = int(input())

for i in range(n):
    line = sys.stdin.readline()
    line = line[:-1]
    if line[0:9] == 'push_back':
        push_back(int(line[10:]))
    elif line[0:10] == 'push_front':
        push_front(int(line[11:]))
    elif line[0:5] == 'front':
        front()
    elif line[0:4] == 'back':
        back()
    elif line[0:5] == 'empty':
        empty()
    elif line[0:9] == 'pop_front':
        pop_front()
    elif line[0:8] == 'pop_back':
        pop_back()
    elif line[0:4] == 'size':
        size()

