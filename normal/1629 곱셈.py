def func(a, b):
    if b == 1:
        return a % c
    else:
        tmp = func(a, b // 2)
        if b % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

a, b, c = map(int, input().split())

print(func(a, b))
