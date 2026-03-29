def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(signals):
    limit = 1
    for g, y, r in signals:
        limit = lcm(limit, g + y + r)

    for t in range(1, limit + 1):
        ok = True
        for g, y, r in signals:
            T = g + y + r
            if not (g <= t % T < g + y):
                ok = False
                break
        if ok:
            return t+1

    return -1