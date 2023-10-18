a = []
b = []

for _ in range(3):
   x, y = map(int, input().split())
   
   a.append(x)
   b.append(y)

for i in range(3):
    if a.count(a[i]) == 1:
        x = a[i]
    if b.count(b[i]) == 1:
        y = b[i]

print(x, y)
