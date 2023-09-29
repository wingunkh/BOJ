def cut(y, x, length):
    global white, blue
    color = a[y][x]
    
    for i in range(y, y+length):
        for j in range(x, x + length):
            if a[i][j] != color:
                cut(y, x, length // 2)
                cut(y + length // 2, x, length // 2)
                cut(y, x + length // 2, length // 2)
                cut(y + length // 2, x + length // 2, length // 2)
                return
    else:
        if color == 0:
            white += 1
        else:
            blue += 1
                
n = int(input())
a = []
white = 0
blue = 0

for _ in range(n):
    a.append(list(map(int, input().split())))

cut(0, 0, n)
print(white)
print(blue)
