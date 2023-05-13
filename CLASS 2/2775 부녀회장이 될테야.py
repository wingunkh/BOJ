def func(a: int, b: int):
    f = [i for i in range(1, b+1)]

    for i in range(a):
        for j in range(1, b):
            f[j] += f[j - 1]

    print(f[-1])
            
t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    func(k,n)
