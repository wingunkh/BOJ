n, m = map(int, input().split())
result = ""

while n:
    remainder = n % m
    n = n // m

    if remainder < 10:
        result += str(remainder)
    else:
        result += chr(remainder + 55)

print(result[::-1])
