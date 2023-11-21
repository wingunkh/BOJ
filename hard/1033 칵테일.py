n = int(input())
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
ratio = [0 for _ in range(n)]
lcm = 1
GCD = 0

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        next = i[0]
        if not visited[next]:
            ratio[next] = ratio[v] * i[2] // i[1]
            dfs(next)
            
for _ in range(n-1):
    a, b, p, q = map(int, input().split())
    
    graph[a].append((b, p, q))
    graph[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))

ratio[0] = lcm
GCD = lcm
dfs(0)

for i in range(1, n):
    GCD = gcd(GCD, ratio[i])

for i in range(n):
    print(ratio[i] // GCD, end = ' ')
