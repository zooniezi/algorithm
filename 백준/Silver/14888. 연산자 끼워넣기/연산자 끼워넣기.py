import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
operator = list(map(int,input().split()))

maxi = -(10**9)
mini = 10**9

def dfs(level, total, plus, minus, mul, div):
    global maxi,mini,N
    if level == N:
        maxi = max(maxi, total)
        mini = min(mini, total)
        return
    
    if plus:
        dfs(level+1, total+nums[level], plus-1, minus, mul, div)
    if minus:
        dfs(level+1, total-nums[level], plus, minus-1, mul, div)
    if mul:
        dfs(level+1, total*nums[level], plus, minus, mul-1, div)
    if div and total<0:
        dfs(level+1, -(-total//nums[level]), plus, minus, mul, div-1)
    if div and total>=0:
        dfs(level+1, total//nums[level], plus, minus, mul, div-1)

dfs(1,nums[0],operator[0],operator[1],operator[2],operator[3])
print(maxi)
print(mini)