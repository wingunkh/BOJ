def binary_search(start, end):
    while start <= end:
        center = (start + end) // 2
        buff = 0
        count = 0
        
        for i in a:
            if buff + i > center:
                count += 1
                buff = 0
            buff += i
        else:
            if buff > 0:
                count += 1

        if count <= m:
            end = center-1
        else:
            start = center+1

    return start

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(binary_search(max(a), sum(a)))
