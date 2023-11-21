import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()
# 우선순위 큐는 내부적으로 최소 힙을 사용하기 때문에 해당 큐는 오름차순으로 정렬된다.

for _ in range(n):
    request = int(input())

    if request != 0:
        pq.put((abs(request), request))
    else:
        if pq.empty():
            print('0')
        else:
            tmp = pq.get() # 가장 높은 우선순위를 가진 요소를 제거 후 반환
            print(tmp[1])
