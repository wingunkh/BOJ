array = []

for _ in range(10):
    a = int(input())
    if a%42 not in array:
        array.append(a%42)

print(len(array))
