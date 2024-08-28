n,m = map(int,input().split())

def permute(n,m):
    used = [0 for i in range(n)]

    def generate(choose, used):
        if len(choose)==m:
            print(*choose)
            return
        for i in range(n):
            if used[i]==0:
                used[i]=1
                choose.append(i+1)
                generate(choose,used)
                used[i]=0
                choose.pop()
            else:
                continue
    generate([],used)

permute(n,m)
