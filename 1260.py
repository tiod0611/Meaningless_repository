# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1260from collections import deque

def dfs(graph, start_node):
    visited = []
    need_visit = []

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node], reverse=True))

    return visited

def bfs(graph, start_node):
    visited = []
    need_visit = deque()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node]))

    return visited

n, m, v = map(int, input().split())

graph = {}
for i in range(1, n+1):
    graph[i] = []
for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(*dfs(graph, v))
print(*bfs(graph, v))