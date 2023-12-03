import sys, heapq
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    number = int(input())
    
    if number > 0:
        heapq.heappush(a, -number)
    else:
        if a:
            print(abs(heapq.heappop(a)))
        else:
            print(0)
