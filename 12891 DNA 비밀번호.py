n, m = map(int, input().split())
a = input()
acgt = list(map(int, input().split()))
start = 0
end = m-1
a_count = a[start:end+1].count('A')
c_count = a[start:end+1].count('C')
g_count = a[start:end+1].count('G')
t_count = a[start:end+1].count('T')
result = 0

while True:
    if a_count >= acgt[0] and c_count >= acgt[1] and g_count >= acgt[2] and t_count >= acgt[3]:
        result += 1

    start += 1
    end += 1

    if end == len(a):
        break

    if a[start-1] == 'A':
        a_count -= 1
    elif a[start-1] == 'C':
        c_count -= 1
    elif a[start-1] == 'G':
        g_count -= 1
    else:
        t_count -= 1

    if a[end] == 'A':
        a_count += 1
    elif a[end] == 'C':
        c_count += 1
    elif a[end] == 'G':
        g_count += 1
    else:
        t_count += 1

print(result)
