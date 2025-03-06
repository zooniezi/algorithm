n,x,k = map(int,input().split())
ball = [0 for i in range(n+1)]
ball[x]=1
for i in range(k):
    a,b = map(int,input().split())
    temp = ball[a]
    ball[a]=ball[b]
    ball[b]=temp

for i in range(n+1):
    if ball[i] == 1:
        print(i)
        break