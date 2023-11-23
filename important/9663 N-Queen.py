def dfs(x):
    global result
    
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if check(x): # 백트래킹
                dfs(x+1)

def check(x):
    for i in range(x):
        if row[x] == row[i]: # 열 검사
            return False
        if x - i == abs(row[x] - row[i]): # 대각선 검사
            return False
    return True
    
n = int(input())
row = [0 for _ in range(n)] # row[i] = j는 퀸을 i행 j열에 놓겠다는 의미
result = 0

dfs(0)

print(result)
