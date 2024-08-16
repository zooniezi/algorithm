n = int(input())

lagrange = [0 for _ in range(50001)]

square = [i*i for i in range(1,224)]
square2 = []
for each1 in square:
    lagrange[each1] = 1
    for each2 in square:
        if each1+each2<50001 and lagrange[each1+each2] == 0:
            lagrange[each1+each2] = 2
            square2.append(each1+each2)

for each in square2:
    for each2 in square:
        if each+each2<50001 and lagrange[each+each2] == 0:
            lagrange[each+each2] = 3

if lagrange[n] == 0:
    print(4)
else:
    print(lagrange[n])
