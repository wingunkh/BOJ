import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    global answer
    visited[v] = True

    for i in a[v]:
        if not visited[i]:
            check[i] = (check[v]+1) % 2 # 인접 노드는 같은 집합이 아니므로 다른 집합으로 처리
            dfs(i)
        elif check[i] == check[v]:
            answer = False
    
n = int(input())

for _ in range(n):
    V, E = map(int, input().split())
    a = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    check = [0 for _ in range(V+1)]
    answer = True

    for _ in range(E):
        s, e = map(int, input().split())
        a[s].append(e)
        a[e].append(s)

    for i in range(1, V+1):
        if answer:
            dfs(i)
        else:
            print("NO")
            break
    else:
        print("YES")
