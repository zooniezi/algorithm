import sys

a = int(input())
people = []
for i in range(a):
    people.append(list(map(int, sys.stdin.readline().split())))

check = [0 for i in range(a)]

for i in range(a):
    now_person = people[i] 
    for compared_person in people:
        if now_person[0] < compared_person[0] and now_person[1] < compared_person[1]:
            check[i]+=1

for i in range(a):
    print(check[i]+1,end=" ")