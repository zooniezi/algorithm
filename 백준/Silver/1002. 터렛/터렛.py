t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
    sum_r2 = (r1 + r2) ** 2
    diff_r2 = (r1 - r2) ** 2

    if d2 == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d2 > sum_r2:
            print(0)
        elif d2 < diff_r2:
            print(0)
        elif d2 == sum_r2 or d2 == diff_r2:
            print(1)
        else:
            print(2)