array = [int(input()) for _ in range(9)] # list comprehension

max = 0
for i in array:
    if i > max:
        max = i

print(max)
print(array.index(max) + 1)
