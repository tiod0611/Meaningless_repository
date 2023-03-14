# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1167

import sys
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(1, len(data)-1, 2):
        graph[data[0]].append((data[j], data[j+1]))


def bfs(start):
    visited = [-1] * (n+1)
    max_node, max_distance = 0, 0
    queue = deque([(start, 0)]) 
    visited[start] = 0
    
    while queue:
        node, distance = queue.popleft()
        for next_node, weight in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = distance + weight
                queue.append((next_node, visited[next_node]))
                if visited[next_node] > max_distance:
                    max_distance = visited[next_node]
                    max_node = next_node
    
    return max_node, max_distance


node, distance = bfs(1)
node, distance = bfs(node)

print(distance)