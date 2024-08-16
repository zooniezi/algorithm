x, y = map(int,input().split())
nowx, nowy = map(int,input().split())

t = int(input())

ansx = 0
ansy = 0

right_left = ((t+nowx)//x)%2
up_down = ((t+nowy)//y)%2

right_left_remain = (t+nowx)%x
up_down_remain = (t+nowy)%y


if right_left == 0:
    ansx = right_left_remain
else:
    ansx = x-right_left_remain

if up_down == 0:
    ansy = up_down_remain
else:
    ansy = y-up_down_remain

print(ansx, ansy)