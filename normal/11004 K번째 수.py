def quick_sort(start, end):
    pl = start
    pr = end
    pivot = a[(pl+pr) // 2]

    while pl <= pr:
        while a[pl] < pivot:
            pl += 1
        while a[pr] > pivot:
            pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
            
    if start < pr:
        quick_sort(start, pr)
    if pl < end:
        quick_sort(pl, end)
    
n, k = map(int, input().split())
a = list(map(int, input().split()))

quick_sort(0, len(a)-1)

print(a[k-1])
