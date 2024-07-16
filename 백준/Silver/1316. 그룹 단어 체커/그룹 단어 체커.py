def groupword(a):
    for i in range(0,len(a)-1):
        if a[i] != a[i+1]:
            new = a[i+1:]
            if new.count(a[i])>0:
                return -1
    return 1

t = int(input())
cnt = 0
for i in range(t):
    word = input()
    if groupword(word)==1:
        cnt+=1
print(cnt)