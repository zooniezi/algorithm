n,m= map(int,input().split())

arr = list(map(int,input().split()))
visited = [0 for i in range(n)]
arr.sort()

def permute(arr,depth,m,result,visited):
    if depth == m:
        print(*result)
        return
    for i in range(len(arr)):
        if visited[i]:
            continue
        if i>0 and arr[i]==arr[i-1] and not visited[i-1]:
            continue

        visited[i] = 1
        permute(arr,depth+1,m,result+[arr[i]],visited)
        visited[i] = 0
permute(arr,0,m,[],visited)