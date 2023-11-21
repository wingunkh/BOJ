import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    q = deque(a)
    count = 0
    
    while q:
        maximum = max(q)
        target = q.popleft()
        m -= 1
        
        if target == maximum:
            count += 1
            if m == -1:
                print(count)
                break
        else:
            q.append(target)
            if m == -1:
                m = len(q)-1
