import sys, heapq
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    x = int(input())
    if not x: # x가 0일 때
        if not q: print(0) # 우선순위 큐가 비었을 때
        else: print(heapq.heappop(q))
    else:
        heapq.heappush(q, x)
