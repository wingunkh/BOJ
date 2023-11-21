import sys
input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                return False
        else:
            return True

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 0 or n == 1:
        print(2)
        continue
    
    while True:
        if is_prime(n):
            print(n)
            break
        else:
            n += 1
