n = int(input())
honeycomb = 1
cnt = 1

while honeycomb < n:
    honeycomb += 6 * cnt
    cnt += 1

print(cnt)
