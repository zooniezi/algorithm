import sys
input = sys.stdin.readline
n = int(input())
child = {}

for i in range(n):
    parent, node1, node2 = map(str, input().split())
    child[parent] = [node1,node2]

ans = []
def search_forward(now_node_letter):
    if now_node_letter == ".":
        return
    ans.append(now_node_letter)
    search_forward(child[now_node_letter][0])
    search_forward(child[now_node_letter][1])

def search_middle(now_node_letter):
    if now_node_letter == ".":
        return
    search_middle(child[now_node_letter][0])
    ans.append(now_node_letter)
    search_middle(child[now_node_letter][1])
    
def search_backward(now_node_letter):
    if now_node_letter == ".":
        return
    search_backward(child[now_node_letter][0])
    search_backward(child[now_node_letter][1])
    ans.append(now_node_letter)

search_forward('A')
print("".join(ans))
ans = []
search_middle('A')
print("".join(ans))
ans = []
search_backward('A')
print("".join(ans))
