import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(1, N+1):
    a = input().strip()
    dic[i] = a
    dic[a] = i

for _ in range(M):
    target = input().strip()

    try:
        print(dic.get(int(target)))
    except:
        print(dic.get(target))
