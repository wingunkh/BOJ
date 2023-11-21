import sys
input = sys.stdin.readline

n = int(input())
a = []
buff = 0
result = 0

for _ in range(n):
    s, e = map(int, input().split())
    a.append((s, e))

# 종료 시간(e) 기준으로 오름차순 정렬
# 종료 시간(e)이 같을 때 사작 시간(s)을 기준으로 오름차순 정렬
a.sort(key = lambda x: (x[1], x[0]))

for i in a:
    if i[0] >= buff:
        result += 1
        buff = i[1]

print(result)
