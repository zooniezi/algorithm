n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
ans = []
def seq(start_idx):

    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(0,n):
        if arr[i] in ans:
            continue
        ans.append(arr[i])
        seq(i+1)
        ans.pop()
    

seq(0)