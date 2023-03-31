# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1389import sys

# 무한대를 의미하는 변수 INF를 설정
INF = sys.maxsize

# 정점의 개수와 간선의 개수 입력 받기
n, m = map(int, input().split())

# 최단 거리 테이블을 모두 무한대로 초기화
dist = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 경우의 최단 거리는 0으로 초기화
for i in range(1, n+1):
    dist[i][i] = 0

# 각 간선의 정보를 입력 받아 최단 거리 테이블 초기화
for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

# 플로이드-와샬 알고리즘을 통해 최단 거리 테이블 계산
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 케빈 베이컨의 수가 가장 작은 사람을 찾아 출력
min_kevin = INF
min_person = 0
for i in range(1, n+1):
    # i번 사람이 다른 사람들과의 케빈 베이컨의 수 합 구하기
    kevin = sum(dist[i][1:n+1])
    # 케빈 베이컨의 수가 더 작은 경우 갱신
    if kevin < min_kevin:
        min_kevin = kevin
        min_person = i

print(min_person)