import sys
import heapq

input = sys.stdin.readline

INF = float('inf')

city_num = int(input())  # 도시 수
bus_num = int(input())  # 버스 수

# 그래프 초기화 (무한대 값으로 설정)
graph = [[] for _ in range(city_num + 1)]
minimum_value = [INF] * (city_num + 1)

# 간선 입력 받기
for _ in range(bus_num):
    a, b, distance = map(int, input().split())
    graph[a].append((b, distance))

start_city, goal_city = map(int, input().split())

# 다익스트라 알고리즘 (우선순위 큐 사용)
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))  # (비용, 노드)
    minimum_value[start] = 0

    while pq:
        current_dist, now = heapq.heappop(pq)

        # 이미 처리된 경우 스킵
        if minimum_value[now] < current_dist:
            continue

        for next_node, weight in graph[now]:
            new_dist = current_dist + weight

            if new_dist < minimum_value[next_node]:  # 더 짧은 경로 발견
                minimum_value[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

# 실행
dijkstra(start_city)

# 결과 출력
print(minimum_value[goal_city])
