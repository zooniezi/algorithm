a,b,c = map(int,input().split())
ans = 1
r = a%c
def power(a,b,c):
    if b==0:
        return 1
    if b==1:
        return (a)%c
    
    half = power(a,b//2,c)
    half = (half%c * half%c)%c

    if b%2 == 0:
        return half
    if b%2 == 1:
        return (half*(a%c))%c
    
print(power(a,b,c))