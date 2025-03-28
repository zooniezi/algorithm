n = int(input())
word = input()
check = [0,0,0]
for i in word:
    if i == 'S':
        check[0]+=1
    elif i=='B':
        check[1]+=1
    elif i=='A':
        check[2]+=1

if check[0]==check[1] and check[1]==check[2]:
    print('SCU')

if check[0]==check[1] and check[1]> check[2]:
    print('BS')

if check[0]==check[2] and check[2]>check[1]:
    print('SA')
if check[1]==check[2] and check[2]>check[0]:
    print('BA')

if check[2]>check[1] and check[2]>check[0]:
    print('A')
if check[1]>check[2] and check[1]>check[0]:
    print('B')
if check[0]>check[1] and check[0]>check[2]:
    print('S')
    