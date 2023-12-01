def dfs(v):
    global result
    count = 0
    
    for i in a[v]:
        if i == target:
            continue
        else:
            count += 1
            dfs(i)
    else:
        if count == 0:
            result += 1
        
n = int(input())
a = [[] for _ in range(n)]
parent = list(map(int, input().split()))
root = 0
target= 0
result = 0

for i in range(n):
    if parent[i] != -1:
        a[parent[i]].append(i)
    else:
        root = i
        
target = int(input())

if target == root:
    print(0)
else:
    dfs(root)
    print(result)
