s = input()
a = set()

for i in range(len(s)):
    for j in range(len(s) - i):
        a.add(s[j:j+i+1])

print(len(a))
