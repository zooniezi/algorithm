n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]

def permute(arr,m):
    used = [0 for _ in range(n)]
    def generate(chosen, used):
        if len(chosen)==m:
            sorted(chosen)
            print(*chosen)
            return
        
        start_idx = arr.index(chosen[-1]) if chosen else 0
        for i in range(start_idx,len(arr)):
            if used[i]==0:
                chosen.append(i+1)
                used[i]=1
                generate(chosen,used)
                used[i]=0
                chosen.pop()
    generate([],used)
permute(arr,m)