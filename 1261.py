# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1261

import heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]

INF = int(1e9)

n, m = map(int, input().split())

graph = []
for i in range(m):
    graph.append(list(map(int,input())))

distance = [[INF] * n for _ in range(m)]

def dijkstra():
    q = []
    heapq.heappush(q,(0,0,0))
    distance[0][0] = 0
    
    while q:
        dist, x, y = heapq.heappop(q)
        
        if distance[x][y] < dist:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            cost = dist + graph[nx][ny]
            
            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heapq.heappush(q,(cost,nx,ny))

dijkstra()

print(distance[m-1][n-1])