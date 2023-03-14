while True:
    array = list(map(int, input().split()))

    if array == [0, 0, 0]:
        break
    
    array.sort()

    if array[0] ** 2 + array[1] ** 2 == array[2] ** 2:
        print("right")
    else:
        print("wrong")
