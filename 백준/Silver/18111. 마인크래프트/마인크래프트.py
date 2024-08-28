import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())
ground = [list(map(int, input().split())) for i in range(n)]

total = 0
for i in range(n):
    total+=sum(ground[i])

max_height = (total+b)//(n*m)
min_time = 1000000000
possible_max_height = 0

for now_height in range(max_height+1):
    temp_b = b
    temp_time = 0
    check = False
    for i in range(n):
        for j in range(m):
            if ground[i][j] > now_height:
                temp_b+=(ground[i][j]-now_height)
                temp_time+=2*(ground[i][j]-now_height)
    
    for i in range(n):
        if check:
            break
        for j in range(m):
            if ground[i][j] < now_height:
                temp_b-=(now_height-ground[i][j])
                if temp_b < 0:
                    check = True
                    break
                temp_time+=(now_height-ground[i][j])
    
    if check:
        continue

    min_time = min(min_time, temp_time)
    if min_time == temp_time:
        possible_max_height = now_height


print(min_time, possible_max_height)