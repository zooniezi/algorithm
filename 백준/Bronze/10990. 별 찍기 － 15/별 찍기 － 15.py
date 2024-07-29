n = int(input())

blank = " "
star = "*"

for i in range(1,n+1):
    if i==1:
        print(blank*(n-i) + star)
    else:
        print(blank*(n-i)+star+blank*(2*i-3)+star)