import sys
list = []
while True:
    try:
        check = [0 for i in range(4)]
        line = input()
        for i in line:
            if ord(i) == 32:
                check[3] += 1
            elif ord(i) >= 65 and ord(i) < 97:
                check[1] += 1
            elif ord(i) >= 97 and ord(i) < 129:
                check[0] += 1
            elif ord(i) >= 48 and ord(i) <= 57:
                check[2] += 1
        for num in check:
            print(num, end=" ")
        print()
    except EOFError:
        break
