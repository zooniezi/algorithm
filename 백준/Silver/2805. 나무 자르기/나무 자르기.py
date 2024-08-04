N, M = map(int, input().split())

trees = list(map(int, input().split()))
max_height = max(trees)

def binary_search(start, end, amount):
  while start <= end:

    mid = (start+end)//2
    count = 0

    for i in range(N):
      if trees[i] > mid:
        count += trees[i]-mid

    if count < amount:
      end = mid - 1
    else:
      start = mid + 1
  return end

print(binary_search(0,max_height,M))
