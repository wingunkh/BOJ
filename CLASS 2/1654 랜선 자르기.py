def binary_search(a: list, n: int) -> int:
    pl = 1
    pr = sum(a) // n
    
    while True:
        pc = (pl + pr) // 2
        cnt = 0
        
        for i in a:
            cnt += i // pc

        if cnt >= n:
            pl = pc + 1
        else:
            pr = pc -1
        if pl > pr:
            return pr
    return -1

k, n = map(int, input().split())
array = [int(input()) for _ in range(k)]

print(binary_search(array, n))
