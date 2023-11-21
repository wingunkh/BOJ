import sys
input = sys.stdin.readline

a = [i for i in range((123456 * 2)+1)]
a[1] = 0

for i in range(2, int(len(a) ** 0.5)+1):
    if a[i] == 0:
        continue
    
    for j in range(i+i, len(a), i):
        a[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    count = 0

    for i in range(n+1, (2 * n)+1):
        if a[i] != 0:
            count += 1

    print(count)
