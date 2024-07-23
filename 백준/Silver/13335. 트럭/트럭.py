from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * w)
current_weight = 0
time = 0

for truck in trucks:
    while True:
        # 시간을 1 증가시키고, 다리에서 트럭 하나를 뺀다
        time += 1
        current_weight -= bridge.popleft()
        
        # 트럭이 다리에 올라갈 수 있는지 확인
        if current_weight + truck <= L:
            bridge.append(truck)
            current_weight += truck
            break
        else:
            bridge.append(0)

# 모든 트럭이 다리를 건넌 후, 다리 위에 남은 트럭이 다리를 건너는 시간 추가
time += w

print(time)