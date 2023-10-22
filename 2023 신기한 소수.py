import sys
sys.setrecursionlimit(10**6)

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                return False
        else:
            return True

def dfs(v):
    if len(str(v)) == n:
        print(v)
    else:
        for i in range(1, 10):
            if is_prime(v * 10 + i):
                dfs(v * 10 + i)

n = int(input())

dfs(2)
dfs(3)
dfs(5)
dfs(7)
