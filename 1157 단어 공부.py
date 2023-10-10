word = input().upper()
alphabet = list(set(word))
cnt = []

for i in alphabet:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) == 1:
    print(alphabet[cnt.index(max(cnt))])
else:
    print("?")
