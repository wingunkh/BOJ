n = int(input())
a = []

for _ in range(n):
    s = input()
    a.append(s)

a = set(a)
a = list(a)
a.sort()
a.sort(key = len)

for i in a:
    print(i)
