def dfs(index, depth):
    if depth == n:
        if check():
            print(*password, sep = '')
        return

    for i in range(index, m):
        password.append(a[i])
        dfs(i+1, depth+1)
        password.pop()

def check():
    count = 0
    
    for i in password:
        if i in aeiou:
            count += 1

    if count >= 1 and n - count >= 2:
        return True
    else:
        return False

n, m = map(int, input().split())
a = sorted(list(input().split()))
aeiou = ['a', 'e', 'i', 'o', 'u']
password = []

dfs(0, 0)
