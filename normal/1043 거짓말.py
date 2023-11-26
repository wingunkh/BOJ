import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return parent[a]
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
truth = list(map(int, input().split()))
del truth[0]
parties = []
result = 0

for _ in range(m):
    buff = list(map(int, input().split()))
    del buff[0]
    parties.append(buff)

for party in parties:
    for j in range(len(party)-1):
        union(party[j], party[j+1])

for party in parties:
    target = party[0]
    for j in truth:
        if find(target) == find(j):
            break
    else:
        result += 1

print(result)
