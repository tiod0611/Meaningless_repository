# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1238import heapq

# 무한대를 나타내는 값
INF = int(1e9)

# n: 학생 수, m: 도로 수, x: 파티가 열리는 마을 번호
n, m, x = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 그래프 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드에서 각 노드까지의 최단 거리
    distance = [INF] * (n + 1)
    distance[start] = 0
    # 최소 힙
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

# 파티까지 가는 거리와 파티에서 각 마을까지 오는 거리를 더한 값 중 최댓값이 정답
result = 0
for i in range(1, n + 1):
    go = dijkstra(i)[x] # 파티까지 가는 거리
    come = dijkstra(x)[i] # 파티에서 i번 마을까지 오는 거리
    result = max(result, go + come)

print(result)