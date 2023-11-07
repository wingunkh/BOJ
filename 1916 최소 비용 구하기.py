import sys, heapq
input = sys.stdin.readline

v = int(input())
e = int(input())
a = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
distance = [sys.maxsize for _ in range(v+1)]
pq = []

for _ in range(e):
    s, e, w = map(int, input().split())
    a[s].append((e, w))

start, end = map(int, input().split())
distance[start] = 0
heapq.heappush(pq, (0, start))

while len(pq) > 0:
    _, now = heapq.heappop(pq)
    if visited[now]:
        continue
    visited[now] = True
    
    for i in a[now]:
        next, weight = i
        if distance[next] > distance[now] + weight:
            distance[next] = distance[now] + weight
            heapq.heappush(pq, (distance[next], next))

print(distance[end])
