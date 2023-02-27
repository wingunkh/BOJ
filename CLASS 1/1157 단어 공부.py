word = input().upper()
alphabet = [0] * 26

for i in word:
    alphabet[ord(i) - 65] += 1

if alphabet.count(max(alphabet)) == 1:
    print(chr(alphabet.index(max(alphabet)) + 65))

else:
    print("?")
