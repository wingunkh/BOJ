n, b = map(int, input().split())
s = ""

while n:
    remainder = n % b
    if remainder < 10:
        s += (str(n % b))
    else:
        s += (chr(n % b + 55))
    n = n // b

print(s[::-1])
