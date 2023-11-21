import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, depth):
    global result
    
    if depth == 5:
        result = True
        return
        
    visited[v] = True

    for i in a[v]:
        if not visited[i]:
            dfs(i, depth+1)
        
    visited[v] = False
                
n, m = map(int, input().split())
a = [[] for _ in range(n)]
visited = [False for _ in range(n)]
result = False

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(n):
    dfs(i, 1)
    
    if result == True:
        print(1)
        break
else:
    print(0)
