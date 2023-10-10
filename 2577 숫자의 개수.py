a, b, c = int(input()), int(input()), int(input())
result = str(a * b * c)

for i in range(10):
    print(result.count(str(i)))
