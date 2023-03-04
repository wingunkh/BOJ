def prime_number(a: int) -> None:
    if a == 1:
        return 0
        
    for i in range(2, int(a**0.5)+1, 1):
        if a % i == 0:
            break
    else:
        print(a)

n, m = map(int, input().split())

for i in range(n, m+1):
    prime_number(i)
