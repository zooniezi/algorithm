B = int(input())

b_arr = list(map(int, input().split()))
a_arr = []

sum_a = 0
for i in range(B):
    a = b_arr[i] * (i + 1) - sum_a
    a_arr.append(a)
    sum_a += a

print(' '.join(map(str, a_arr)))
