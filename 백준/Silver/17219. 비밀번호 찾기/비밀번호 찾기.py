import sys

n,m = map(int, input().split())
dict = {}

for _ in range(n):
    now_line = sys.stdin.readline()
    now_line = now_line[:-1]
    site, password = now_line.split()
    dict[site] = password

for _ in range(m):
    print(dict[sys.stdin.readline()[:-1]])
