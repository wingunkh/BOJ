import sys
input = sys.stdin.readline

N = int(input())
meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key = lambda x: (x[1], x[0]))
# x에는 meetings 리스트의 각 요소가 전달된다.

last = 0
cnt = 0

for start, end in meetings:
    if start >= last:
        last = end
        cnt += 1

print(cnt)
