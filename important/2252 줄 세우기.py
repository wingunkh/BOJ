import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)] # 진입 차수 리스트
q = deque()

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    indegree[e] += 1 # 그래프 구현과 동시에 진입 차수 증가

for i in range(1, n+1):
    if indegree[i] == 0: # 진입 차수가 0인 노드의 경우
        q.append(i) # 큐에 저장

while q:
    now = q.popleft()
    print(now, end = ' ') # 진입 차수가 0인 노드를 큐에서 제거하면서 출력
    
    for next in a[now]: # 큐에서 제거된 노드가 가리키는 노드들의 경우
        indegree[next] -= 1 # 진입 차수 1씩 감소
        if indegree[next] == 0:
            q.append(next)
