def solution(k, d):
    ans = 0
    for y in range(0, d + 1, k):
        max_x = int((d*d - y*y) ** 0.5)
        ans += max_x // k + 1
    return ans
    