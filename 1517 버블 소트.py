def merge_sort(start, end):
    global count
    
    if start >= end:
        return
    else:
        center = (start + end) // 2

        merge_sort(start, center)
        merge_sort(center+1, end)

        i = start
        p1, p2 = start, center+1

        while p1 <= center and p2 <= end:
            if a[p1] <= a[p2]:
                buff[i] = a[p1]
                i += 1
                p1 += 1
            else:
                buff[i] = a[p2]
                count += (p2 - i)
                i += 1
                p2 += 1
        else:
            buff[i:end+1] = a[p1:center+1] + a[p2:end+1]

        for i in range(start, end+1):
            a[i] = buff[i]

n = int(input())
a = list(map(int, input().split()))
buff = [0 for _ in range(len(a))]
count = 0

merge_sort(0, len(a)-1)

print(count)
