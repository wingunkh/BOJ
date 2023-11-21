import heapq

n = int(input())
plus = []
minus = []
one = 0
zero = 0
result = 0

for _ in range(n):
    data = int(input())
    
    if data > 1:
        heapq.heappush(plus, -data)
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        heapq.heappush(minus, data)

while len(plus) > 1:
    a = heapq.heappop(plus)
    b = heapq.heappop(plus)
    result += a * b

if len(plus) > 0:
    result += -heapq.heappop(plus)

while len(minus) > 1:
    a = heapq.heappop(minus)
    b = heapq.heappop(minus)
    result += a * b

if len(minus) > 0:
    if zero == 0:
        result += heapq.heappop(minus)

print(result + one)
