import sys
input = sys.stdin.readline

def dfs(index, depth):
    global result
    
    if depth == m:
        buff = 0
        
        for r1, c1 in house:
            distance = sys.maxsize
            
            for i in range(len(chicken)):
                if visited[i]:
                    distance = min(distance, abs(r1 - chicken[i][0]) + abs(c1 - chicken[i][1]))

            buff += distance

        result = min(result, buff)

        return
                    
    for i in range(index, len(chicken)):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, depth+1)
            visited[i] = False
        
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
result = sys.maxsize

for r in range(n):
    for c in range(n):
        if a[r][c] == 1:
            house.append((r, c))
        elif a[r][c] == 2:
            chicken.append((r, c))

visited = [False for _ in range(len(chicken))]

dfs(0, 0)

print(result)
