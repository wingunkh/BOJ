n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0

for i in range(len(a)):
    start = 0
    end = len(a)-1
    
    while start < end:
        if a[start] + a[end] < a[i]:
            start += 1
        elif a[start] + a[end] > a[i]:
            end -= 1
        else:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                count += 1
                break

print(count)
