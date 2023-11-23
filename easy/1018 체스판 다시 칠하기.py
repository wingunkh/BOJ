n, m = map(int, input().split())
a = []
result = []

for _ in range(n):
    a.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        case_black = 0
        case_white = 0
        
        for r in range(i, i+8):
            for c in range(j, j+8):
                if (r+c) % 2 == 0:
                    if a[r][c] == 'B':
                        case_white += 1
                    else:
                        case_black += 1
                else:
                    if a[r][c] == 'W':
                        case_white += 1
                    else:
                        case_black += 1
                        
        result.append(min(case_black, case_white))

print(min(result))
