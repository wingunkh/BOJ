def binary_search(a: list, key: int) -> None:
    pl = 0
    pr = len(a) -1

    while True:
        pc = (pl + pr) // 2

        if a[pc] == key:
            print("1")
            break
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            print("0")
            break
            
n  = int(input())
an = list(map(int, input().split()))
an.sort()

m = int(input())
am = list(map(int, input().split()))

for i in am:
    binary_search(an, i)
