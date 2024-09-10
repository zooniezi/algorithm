n,m = map(int,input().split())
ans = []
def permute(idx):
    global n
    global m
    if len(ans) == m:
        print(*ans)
        return
    for i in range(idx,n+1):
        ans.append(i)
        permute(i)
        ans.pop()

permute(1)