import sys
input = sys.stdin.readline

n = int(input())
a = []
dic = dict()

for _ in range(n):
    a.append(int(input()))

a.sort()

print(int(round(sum(a) / n, 0)))
print(a[n // 2])

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

max_value = max(dic.values())
max_list = []

for i in dic:
    if dic[i] == max_value:
        max_list.append(i)

if len(max_list) > 1:
    print(max_list[1])
else:
    print(max_list[0])
    
print(max(a) - min(a))
