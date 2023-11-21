import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [] # 에지 리스트
distance = [sys.maxsize for _ in range(n+1)]
isNegativeCycle = False # 음수 사이클 유무

for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))
    
distance[1] = 0

# 최단 거리 리스트 업데이트 반복 횟수는 노드 개수 -1이다.
# (특정 두 노드의 최단 거리를 구성할 수 있는 엣지의 최대 개수 = 노드 개수 - 1)
for _ in range(n-1):
    for s, e, w in edges:
        if distance[s] != sys.maxsize and distance[e] > distance[s] + w:
            distance[e] = distance[s] + w

# 음수 사이클 유무를 확인하기 위해 업데이트 재시행
for s, e, w in edges:
    if distance[s] != sys.maxsize and distance[e] > distance[s] + w:
        isNegativeCycle = True
        break

if isNegativeCycle:
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
