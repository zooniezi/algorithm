def hansoo(a):
    check = []
    while True:
        check.append(a%10)
        a = a//10
        if a==0:
            break
    if len(check)!=1:
        compare = check[0]-check[1]
    else:
        return 1
    for i in range(len(check)-1):
        if compare != check[i]-check[i+1]:
            return 0
    return 1

n = int(input())
count = 0
for i in range(1,n+1):
    if hansoo(i)==1:
        count+=1
print(count)
