n = int(input())
title = 666
cnt = 0

while True:
    if "666" in str(title):
        cnt += 1
    if cnt == n:
        break
    title += 1

print(title)
