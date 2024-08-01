n = int(input())

arr = [[" " for _ in range(n)]for _ in range(n)]
y = n
x = 0
while True:
    if y==1:
        break
    y/=3
    x+=1

def star(exponent, x,y):
    if exponent == 1:
        arr[x][y] = "*"
        arr[x][y+1] = "*"
        arr[x][y+2] = "*"
        arr[x+1][y] = "*"
        arr[x+1][y+1] = " "
        arr[x+1][y+2] = "*"
        arr[x+2][y] = "*"
        arr[x+2][y+1] = "*"
        arr[x+2][y+2] = "*"
        return
    else:
        star(exponent-1, x,y)
        star(exponent-1, x,y+3**(exponent-1))
        star(exponent-1, x,y+3**(exponent-1)*2)

        star(exponent-1, x+3**(exponent-1),y)
        star(exponent-1, x+3**(exponent-1),y+3**(exponent-1)*2)

        star(exponent-1, x+3**(exponent-1)*2,y)
        star(exponent-1, x+3**(exponent-1)*2,y+3**(exponent-1))
        star(exponent-1, x+3**(exponent-1)*2,y+3**(exponent-1)*2)

star(x,0,0)
for i in range(n):
    print("".join(arr[i]))