n = int(input())

string = input()
sums = 0

for i in range(n):
    now_letter = ord(string[i])-96
    sums += (now_letter*(31**i))%1234567891
    sums %= 1234567891

print(sums)
