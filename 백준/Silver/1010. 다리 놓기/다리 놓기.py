t = int(input())

def factorial(n):
    if n==1 or n==0:
        return 1
    
    return n*factorial(n-1)


for i in range(t):
    n,m=map(int, input().split())
    mm = factorial(m)
    nn = factorial(n)
    mn = factorial(m-n)
    ans = mm//(nn*mn)
    print(ans)