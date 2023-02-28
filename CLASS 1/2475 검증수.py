array = list(map(int, input().split()))

total = 0
for i in array:
    total += (i ** 2)

print(total % 10)
