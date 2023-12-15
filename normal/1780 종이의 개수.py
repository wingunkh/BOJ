def func(r, c, length):
    start = a[r][c]
    
    for i in range(r, r + length):
        for j in range(c, c + length):
            if a[i][j] != start:
                for k in range(r, r + length, length // 3):
                    for l in range(c, c + length, length // 3):
                        func(k, l, length // 3)
                return
                        
    result[start] += 1

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
result = {-1:0, 0:0, 1:0}

func(0, 0, n)

for i in result.keys():
    print(result[i])
