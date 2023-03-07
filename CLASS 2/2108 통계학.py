import sys

n = int(sys.stdin.readline())
array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))
    
array.sort()
dic = dict()

print(round(sum(array) / n)) # 산술평균 출력

print(array[n // 2]) # 중앙값 출력

for i in array:
    if i in dic: # in 연산자는 딕셔너리에서 키의 멤버십을 판단한다.
        dic[i] += 1
    else:
        dic[i] = 1

max_value = max(dic.values())
max_list = []

for i in dic:
    if dic[i] == max_value:
        max_list.append(i)

if len(max_list) > 1:
    print(max_list[1]) # 최빈값 중 두 번째로 작은 값 출력
else:
    print(max_list[0]) # 최빈값 출력

print(max(array) - min(array))
