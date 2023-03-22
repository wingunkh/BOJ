t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    H = n % h
    W = n // h + 1 # XX0호가 아닌 XX1호부터 시작하므로 1을 더해준다.
    
    if n % h == 0:
        H = h
        W -= 1

    print(H*100 + W)
