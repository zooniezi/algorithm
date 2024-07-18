n = int(input())

for i in range(1,n+1):
    line = [' ' for j in range(2*n-1)]
    if i == 1:
        line[n-1] = '*'
    elif i == n:
        line = ['*' for j in range(2*n-1)]
    else:
        line[n-1-(i-1)] = '*'
        line[n-1+(i-1)] = '*'


    for letter in line[:n+i-1]:
        print(letter, end="")
    if i != n:
        print()