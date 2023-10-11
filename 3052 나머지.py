a = []

for i in range(10):
    a.append(int(input()) % 42)

print(len(set(a)))
