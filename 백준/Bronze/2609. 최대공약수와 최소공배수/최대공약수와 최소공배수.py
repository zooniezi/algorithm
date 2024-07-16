n,m = map(int, input().split())

def Euclide(a,b):
    big = max(a,b)
    small = min(a,b)
    r = big%small
    if r == 0:
        return small
    
    return Euclide(small, r)
gcd = Euclide(n,m)
lcm = (n/gcd) * (m/gcd) * gcd
print(gcd)
print(int(lcm))

