t = int(input())

num = 2

while True:
    if t==1 or t==2:
        print(t)
        break
    num = num*2
    if num>=t:
        print((t-(num//2))*2)
        break
