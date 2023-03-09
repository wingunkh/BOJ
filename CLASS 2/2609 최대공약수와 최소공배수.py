def gcd(x: int, y:int) -> int:
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

def lcm(x: int, y: int, gcd_res: int) -> int:
    return (x * y) // gcd_res

a, b = map(int, input().split())
gcd_res = gcd(a,b) if a > b else gcd(b,a)

print(gcd_res)
print(lcm(a, b, gcd_res))
