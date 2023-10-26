import heapq

n = int(input())
a = []
result = 0

for _ in range(n):
    a.append(int(input()))

heapq.heapify(a)

while len(a) > 1:
    data1 = heapq.heappop(a)
    data2 = heapq.heappop(a)
    result += data1 + data2
    heapq.heappush(a, data1 + data2)

print(result)
