def func(r, c, length):
    buff = []

    for i in range(r, r + length):
        for j in range(c, c + length):
            buff.append(a[i][j])

    if buff == [0 for _ in range(length * length)]:
        print(0, end = '')
        return
    elif buff == [1 for _ in range(length * length)]:
        print(1, end = '')
        return

    print('(', end = '')
    func(r, c, length // 2)
    func(r, c + length // 2, length // 2)
    func(r + length // 2, c, length // 2)
    func(r + length // 2, c + length // 2, length // 2)
    print(')', end = '')

n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input())))

func(0, 0, n)
