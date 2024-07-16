t = int(input())

pool = []

pool.append(666)

for i in range(3000):
  nowPool = []
  nowNum = f"{i:04d}"
  for j in range(4):
    nowPool.append(nowNum[j])
  
  for k in range(5):
    nowPool.insert(k,'666')
    pool.append(int(''.join(nowPool)))
    nowPool.pop(k)

pool = list(set(pool))
pool.sort()
print(pool[t-1])
