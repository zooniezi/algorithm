import sys
input = sys.stdin.readline

n = int(input())
triangle = []

for i in range(n):
    triangle.append(list(map(int,input().split())))

max_sum = [[0 for j in range(i+1)] for i in range(n)]

for i in range(n):
    for j in range(i+1):
        if i == 0:
            max_sum[i][j] = triangle[0][0]
            continue
        else:
            if j == 0:
                max_sum[i][j] = triangle[i][j]+max_sum[i-1][j]
                continue
            if j == i:
                max_sum[i][j] = triangle[i][j]+max_sum[i-1][j-1]
                continue
            max_sum[i][j] = max(triangle[i][j]+max_sum[i-1][j],triangle[i][j]+max_sum[i-1][j-1])

print(max(max_sum[n-1]))