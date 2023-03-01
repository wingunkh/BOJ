n, m = map(int, input().split())
board = [input() for _ in range(n)]
count = []

for a in range(n-7): # 시작점을 정하기 위한 반복문, a는 시작점의 행 좌표
    for b in range(m-7): # 시작점을 정하기 위한 반복문, b는 시작점의 열 좌표
        case_w = 0 # 시작점이 'W'일 경우 바뀌어야 할 보드 칸의 개수 
        case_b = 0 # 시작점이 'B'일 경우 바뀌어야 할 보드 칸의 개수
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 현재 행렬 좌표값의 합이 짝수이면 시작점의 색깔과 같아야 한다.
                    if board[i][j] != 'W':
                        case_w += 1
                    if board[i][j] != 'B':
                        case_b += 1
                else: # 현재 행렬 좌표값의 합이 홀수이면 시작점의 색깔과 달라야 한다.
                    if board[i][j] != 'B':
                        case_w += 1
                    if board[i][j] != 'W':
                        case_b += 1
        count.append(min(case_w, case_b))

print(min(count))
