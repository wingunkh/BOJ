n = int(input())
a = list(map(int, input().split()))
b = sorted(set(a))
dic = {b[i] : i for i in range(len(b))}

for i in a:
    print(dic[i], end = ' ')
