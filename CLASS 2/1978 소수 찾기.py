def prime_number(a: int) -> bool:
    if a == 1:
        return False
    
    for i in range(2, int(a**0.5)+1, 1):
        if a % i == 0:
            return False
    else:
        return True

n = int(input())
array = list(map(int, input().split()))
cnt = 0

for i in array:
    if prime_number(i):
        cnt += 1

print(cnt)
