n = int(input())
arr = [0 for i in range(n+1)]
for i in range(n+1):
    seq = [n]
    next_num = seq[-1]-i
    while True:
        if next_num < 0:
            break
        else:
            seq.append(next_num)
            next_num = seq[-2]-seq[-1]
    arr[i] = seq
maxlen = 1
maxidx = 0
for i in range(n):
    if len(arr[i]) > maxlen:
        maxlen = len(arr[i])
        maxidx = i

print(maxlen)
print(*arr[maxidx])