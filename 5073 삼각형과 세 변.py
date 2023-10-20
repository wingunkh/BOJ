while True:
    a = sorted(list(map(int, input().split())))

    if sum(a) == 0:
        break

    if a[0] + a[1] <= a[2]:
        print("Invalid")
    elif a[0] == a[1] == a[2]:
        print("Equilateral")
    elif a[0] != a[1] and a[1] != a[2] and a[0] != a[2]:
        print("Scalene")
    else:
        print("Isosceles")
