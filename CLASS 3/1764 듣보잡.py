import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
array = []

for _ in range(N + M):
    x = input().strip()
    if dic.get(x) == None:
        dic[x] = 1
    else:
        array.append(x)

array.sort()
print(len(array))
for i in array:
    print(i)
