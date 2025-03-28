p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))
p3 = list(map(int,input().split()))

a1 = p2[0]-p1[0]
a2 = p2[1]-p1[1]

b = a1*p1[1] - a2*p1[0]

if a1*p3[1] == a2*p3[0] + b:
    print(0)

elif a1*p3[1] > a2*p3[0] + b:
    print(1)
elif a1*p3[1] < a2*p3[0] + b:
    print(-1)