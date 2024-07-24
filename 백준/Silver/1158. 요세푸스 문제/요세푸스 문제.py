class Node():
    def __init__(self, num, next, before):
        self.num = str(num)
        self.next = next
        self.before = before

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(Node(i+1,(i+1)%n, (i-1)%n))

ans = []
now = arr[0]

for _ in range(k-1):
    now = arr[now.next]
ans.append(now.num)
arr[now.before].next = now.next
arr[now.next].before = now.before


while len(ans)!=n:
    for _ in range(k):
        now = arr[now.next]
    ans.append(now.num)
    arr[now.before].next = now.next
    arr[now.next].before = now.before

print("<"+", ".join(ans)+">")