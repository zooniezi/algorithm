import sys

n = int(sys.stdin.readline())

height = []
for i in range(n):
    h = int(sys.stdin.readline())
    height.append(h)

# 서쪽의 최대 높이를 저장할 배열
max_west = [0] * n
# 동쪽의 최대 높이를 저장할 배열
max_east = [0] * n

# 첫 번째 원소 처리
max_west[0] = height[0]
# 서쪽의 최대 높이를 미리 계산
for i in range(1, n):
    max_west[i] = max(max_west[i-1], height[i])

# 마지막 원소 처리
max_east[n-1] = height[n-1]
# 동쪽의 최대 높이를 미리 계산
for i in range(n-2, -1, -1):
    max_east[i] = max(max_east[i+1], height[i])

# 결과 출력
for i in range(n):
    print(max_west[i], max_east[i])