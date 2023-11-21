def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
numerator = a1 * b2 + a2 * b1
denominator = b1 * b2
GCD = gcd(numerator, denominator)

print(numerator // GCD, denominator // GCD)
