n = int(input())

for _ in range(n):
    s, e = map(int, input().split())
    distance = e - s
    a = int(distance ** 0.5)
    target = distance - a ** 2
    result = a * 2 - 1

    if target == 0:
        print(result)
    elif target <= a:
        print(result + 1)
    else:
        print(result + 2)
