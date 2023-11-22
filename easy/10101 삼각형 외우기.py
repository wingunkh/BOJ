a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Error")
elif a == b == c:
    print("Equilateral")
elif a != b and b != c and a != c:
    # a != b != c 는 a != b and b != c와 같다.
    # 그러므로 a != b and b != c and a != c가 옳다.
    print("Scalene")
else:
    print("Isosceles")
