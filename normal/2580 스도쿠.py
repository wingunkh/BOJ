import sys

def dfs(depth):
    if depth == len(blank):
        for row in a:
            print(*row, sep = ' ')
        exit(0)
 
    r, c = blank[depth]

    for i in range(1, 10):
        if row_check(r, i) and col_check(c, i) and square_check(r, c, i):
            a[r][c] = i
            dfs(depth+1)
            a[r][c] = 0

def row_check(r, i):
    for c in range(9):
        if a[r][c] == i:
            return False

    return True

def col_check(c, i):
    for r in range(9):
        if a[r][c] == i:
            return False

    return True

def square_check(r, c, i):
    r = r // 3 * 3
    c = c // 3 * 3

    for row in range(r, r+3):
        for col in range(c, c+3):
            if a[row][col] == i:
                return False
            
    return True

a = [list(map(int, input().split())) for _ in range(9)]
blank = []

for r in range(9):
    for c in range(9):
        if a[r][c] == 0:
            blank.append((r, c))

dfs(0)
