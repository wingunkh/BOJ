import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
a = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
distance = [sys.maxsize for _ in range(V+1)] # 출발 노드와 이외의 모든 노드 간의 최단 거리 리스트
pq = [] # 우선순위 큐에 해당 노드까지의 거리와 노드의 번호 저장

for _ in range(E):
    u, v, w = map(int, input().split())
    a[u].append((v, w))

distance[start] = 0 # 출발 노드에서 출발 노드까지의 최단 거리는 0
heapq.heappush(pq, (0, start)) 

while len(pq) > 0:
    _, now = heapq.heappop(pq)
    if visited[now]:
        continue
    visited[now] = True

    for i in a[now]:
        next, weight = i
        if distance[next] > distance[now] + weight: # 최단 거리 갱신
            distance[next] = distance[now] + weight 
            heapq.heappush(pq, (distance[next], next))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
