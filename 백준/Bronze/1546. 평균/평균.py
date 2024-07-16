testcase = int(input())
a = list(map(int, input().split()))
sum = 0
for i in range(testcase):
    sum+=a[i]
maximum = max(a)
print(float((sum/maximum*100))/testcase)