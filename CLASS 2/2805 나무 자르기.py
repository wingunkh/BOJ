import sys

def binary_search(a: list, key: int) -> int:
    pl = 1
    pr = max(a) - 1
    buff = 0

    while True:
        pc = (pl + pr) // 2
        wood = 0

        for i in a:
            if i - pc > 0:
                wood += i - pc
            
        if wood == key:
            return pc
        elif wood < key:
            pr = pc - 1
        else:
            buff = pc
            pl = pc + 1
        if pl > pr:
            break
    return buff
        
n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
print(binary_search(array, m))
