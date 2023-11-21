n = int(input())
a = set(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

for i in b:
    if i in a:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
