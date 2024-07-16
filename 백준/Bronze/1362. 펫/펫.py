life = 1
cnt = 1
while True:
  status = input().split()

  if status[0] == 'F':
    w+=int(status[1])
  elif status[0] == 'E':
    w-=int(status[1])
    if w <= 0:
      life = 0
  elif status[0]!="#":
    o = int(status[0])
    w = int(status[1])
  if status[0] == '0':
    break
  if status[0] == '#':
    print(cnt, end=" ")
    cnt +=1
    if life == 0:
      print("RIP")
    elif w>0.5*o and w<2*o:
      print(":-)")
    else:
      print(":-(")
    life = 1