a = []
result = 0

for _ in range(8):
    a.append(list(input()))

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and a[i][j] == 'F':
            result += 1

print(result)
