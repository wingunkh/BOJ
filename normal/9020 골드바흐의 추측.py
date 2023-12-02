n = int(input())
a = [i for i in range(10001)]
a[1] = 0

for i in range(2, int(len(a) ** 0.5)+1):
    if a[i] == 0:
        continue

    for j in range(i+i, len(a), i):
        a[j] = 0

for _ in range(n):
    number = int(input())
    left = number // 2
    right = number // 2

    while not(a[left] != 0 and a[right] != 0):
        left -= 1
        right += 1

    print(left, right)
