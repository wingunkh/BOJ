def z_order(n, x, y):
    if n == 0:
        return 0

    half = 2**(n-1)

    # 좌상단 분면
    if x < half and y < half:
        return z_order(n-1, x, y)
    # 우상단 분면
    elif x < half and y >= half:
        return half * half + z_order(n-1, x, y - half)
    # 좌하단 분면
    elif x >= half and y < half:
        return 2 * half * half + z_order(n-1, x - half, y)
    # 우하단 분면
    else:
        return 3 * half * half + z_order(n-1, x - half, y - half)

N, r, c = map(int, input().split())
result = z_order(N, r, c)
print(result)
