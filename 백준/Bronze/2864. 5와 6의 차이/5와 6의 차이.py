a,b = map(str,input().split())
maxa,maxb,mina,minb=[],[],[],[]
for i in a:
    if i=='5':
        maxa.append('6')
        mina.append('5')
        continue
    if i=='6':
        mina.append('5')
        maxa.append('6')
        continue
    maxa.append(i)
    mina.append(i)
for i in b:
    if i=='5':
        maxb.append('6')
        minb.append('5')
        continue
    if i=='6':
        minb.append('5')
        maxb.append('6')
        continue
    maxb.append(i)
    minb.append(i)

print(int(''.join(mina))+int(''.join(minb)),int(''.join(maxa))+int(''.join(maxb)))