n = int(input())
diagonal = 1 # 대각선

while diagonal < n:
    n -= diagonal
    diagonal += 1

if diagonal % 2 != 0:
    a = diagonal+1-n
    b = n
else:
    a = n
    b = diagonal+1-n

print(f"{a}/{b}")
