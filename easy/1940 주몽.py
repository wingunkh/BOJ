n = int(input())
m = int(input())
a = list(map(int, input().split()))
a.sort()
start = 0
end = len(a)-1
count = 0

while start < end:
    if a[start] + a[end] < m:
        start += 1
    elif a[start] + a[end] > m:
        end -= 1
    else:
        count += 1
        start += 1
        end -= 1

print(count)
