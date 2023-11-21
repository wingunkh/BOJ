a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Error")
elif a == b == c:
    print("Equilateral")
elif a != b and b != c and a != c: # a != b != c 조건식과 다르다.
    print("Scalene")
else:
    print("Isosceles")
