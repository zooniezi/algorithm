import sys

this_set = [0 for i in range(21)]
this_set[0] = -1
def add(x):
    this_set[x] = 1

def remove(x):
    this_set[x] = 0

def check(x):
    if this_set[x] == 0:
        print(0)
        return
    print(1)

def toggle(x):
    if this_set[x] == 0:
        this_set[x] = 1
        return
    this_set[x] = 0

def all():
    for i in range(1, 21):
        this_set[i] = 1

def empty():
        for i in range(1, 21):
            this_set[i] = 0

n = int(input())

for i in range(n):
    now = sys.stdin.readline()
    if now == 'empty\n':
        empty()
    elif now == 'all\n':
        all()

    else:
        nownum = int(now[-2])
        if now[0] == 'a':
            add(nownum)
        elif now[0] == 'r':
            remove(nownum)
        elif now[0] == 'c':
            check(nownum)
        elif now[0] == 't':
            toggle(nownum)