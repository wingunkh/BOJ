s = input().split('-')
result = 0

for i in s[0].split('+'):
    result += i

for i in s[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
