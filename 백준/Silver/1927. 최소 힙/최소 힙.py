from collections import deque
import sys
input = sys.stdin.readline

def heapup(heap):
    now_index = len(heap) - 1
    while now_index > 0:
        parent_index = (now_index - 1) // 2
        if heap[parent_index] > heap[now_index]:
            heap[parent_index], heap[now_index] = heap[now_index], heap[parent_index]
            now_index = parent_index
        else:
            break

def heapdown(heap):
    now_index = 0
    length = len(heap)
    while (now_index * 2) + 1 < length:
        left_child_index = (now_index * 2) + 1
        right_child_index = (now_index * 2) + 2

        smaller_child_index = left_child_index
        if right_child_index < length and heap[right_child_index] < heap[left_child_index]:
            smaller_child_index = right_child_index
        
        if heap[now_index] > heap[smaller_child_index]:
            heap[now_index], heap[smaller_child_index] = heap[smaller_child_index], heap[now_index]
            now_index = smaller_child_index
        else:
            break

n = int(input())

heap = deque([])

for _ in range(n):
    now = int(input())
    if now == 0:
        if not heap:
            print(0)
        else:
            print(heap[0])
            heap[0] = heap[-1]
            heap.pop()
            heapdown(heap)
    else:
        heap.append(now)
        heapup(heap)
