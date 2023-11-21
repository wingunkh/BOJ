import sys

def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

m = int(input())
n = int(input())
sum = 0
minimum = sys.maxsize

for i in range(m, n+1):
    if is_prime(i):
        sum += i
        if i < minimum:
            minimum = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(minimum)
