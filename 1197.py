# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1197

import sys

# 부모 노드 찾기 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 노드를 연결하는 함수 (Union 연산)
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 받기
V, E = map(int, sys.stdin.readline().split())
edges = []

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

# 크루스칼 알고리즘을 위한 초기화
parent = [i for i in range(V+1)]
edges.sort()    # 가중치 기준으로 간선 정렬
result = 0      # 최종 가중치 값

# 간선 연결 (크루스칼 알고리즘 적용)
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)