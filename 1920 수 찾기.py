def binary_search(n):
    pl = 0
    pr = len(a)-1

    while pl <= pr:
        pc = (pl+pr) // 2

        if a[pc] > n:
            pr = pc-1
        elif a[pc] < n:
            pl = pc+1
        else:
            print(1)
            break
    else:
        print(0)
        
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

for i in b:
    binary_search(i)
