n = int(input())
num = list(range(1,n+1))
num2 = list(range(n-1,0,-1))
final_num = num+num2

asterisk = "*"
for i in final_num:
    print(asterisk*i)