n, m = map(int, input().split())
board = [input() for _ in range(n)]
count = []

for i in range(n-7):
    for j in range(m-7):
        case_white = 0
        case_black = 0
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W': # 시작점이 흰색이라고 가정
                        case_white += 1
                    else: # 시작점이 검은색이라고 가정
                        case_black += 1
                else:
                    if board[a][b] != 'B': # 시작점이 흰색이라고 가정
                        case_white += 1
                    else: # 시작점이 검은색이라고 가정
                        case_black += 1
                        
        count.append(min(case_white, case_black))

print(min(count))
