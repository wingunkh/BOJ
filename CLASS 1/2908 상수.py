a, b = input().split()

a, b = int(a[::-1]), int(b[::-1])

print(a) if a > b else print(b)
