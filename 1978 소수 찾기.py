def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                return False
        else:
            return True

n = int(input())
a = list(map(int, input().split()))
result = 0

for i in a:
    if is_prime(i):
        result += 1

print(result)
