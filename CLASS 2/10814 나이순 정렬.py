n = int(input())

array = []

for i in range(n):
    age, name = input().split()
    array.append([int(age), name])

array.sort(key = lambda x: int(x[0]))
# sort() 함수의 매개변수 key에는 정렬을 목적으로 하는 함수를 값으로 넣는다.
# lambda 인자 : 표현식

for i in range(n):
    print(array[i][0], array[i][1])
