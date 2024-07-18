import sys 

n,m = map(int, input().split())
dict_num = {}
dict_name = {}
for i in range(n):
    now = sys.stdin.readline()
    now = now[:-1]
    dict_num[i+1] = now
    dict_name[now] = i+1

for _ in range(m):
    now = sys.stdin.readline()
    now = now[:-1]
    if now.isdigit():
        print(dict_num[int(now)])
    if now.isalpha():
        print(dict_name[now])