s = input()
alphabet = [-1 for _ in range(26)]

for i in s:
    if alphabet[ord(i)-97] == -1:
        alphabet[ord(i)-97] = s.find(i)

print(*alphabet)
