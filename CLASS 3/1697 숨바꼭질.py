import sys
from collections import deque
input = sys.stdin.readline

def BFS(start: int) -> int:
    q = deque()
    q.append(start)

    while q:
        start = q.popleft()
        if start == K:
            return graph[start]

        for i in [start-1, start+1, start*2]:
            if 0 <= i <= 100000 and not graph[i]:
                graph[i] = graph[start] + 1
                q.append(i)
            
N, K = map(int, input().split())
graph = [0] * 100001

print(BFS(N))
