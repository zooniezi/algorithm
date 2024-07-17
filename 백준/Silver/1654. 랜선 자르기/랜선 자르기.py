import sys

k, n = map(int, sys.stdin.readline().split())
lan = []

# 입력 받기
for i in range(k):
    lan.append(int(sys.stdin.readline()))

maxlan = max(lan)
ans = 0

def check_num_of_lan(lan_list, now_lan_length):
    n = 0
    for i in lan_list:
        n += i//now_lan_length
    return n

def binary_search(start, end):
    if start > end:
        return
    mid = (start+end)//2
    global n
    global ans

    if check_num_of_lan(lan, mid) >= n:
        ans = mid
        binary_search(mid+1, end)
    
    else:
        binary_search(start, mid-1)
        
binary_search(1, maxlan)
print(ans)