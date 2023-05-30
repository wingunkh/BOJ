array = input().split('-')
res = 0

for i in array[0].split('+'):
    res += int(i)

for i in array[1:]:
    for j in i.split('+'):
        res -= int(j)

print(res)
