def gcd(a,b):
    if b==0: return a
    else: return gcd(b, a%b)
testcase = int(input())
for i in range(testcase):
    a,b = map(int, input().split())
    c=gcd(a,b)
    print(a*b//c)
    