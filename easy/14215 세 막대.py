a = sorted(list(map(int, input().split())))

if a[0] + a[1] > a[2]:
    print(sum(a))
else:
    print((a[0] + a[1]) * 2 - 1)
