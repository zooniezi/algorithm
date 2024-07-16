n,m,l = map(int, input().split())
check = []
for i in range(n):
  check.append(0)
check[0]+=1
cnt = 0
index = 0
while True:
  if m == 1:
    print(cnt)
    break
  if check[index]%2 == 1:
    index= (index+l)%n
    cnt+=1
    check[index]+=1
  else:
    index = (index-l)%n
    cnt+=1
    check[index]+=1
  if check[index] == m:
    print(cnt)
    break