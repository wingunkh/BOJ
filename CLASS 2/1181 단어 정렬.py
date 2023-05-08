n = int(input())
array = []

for _ in range(n):
    array.append(input())
    
set_array = set(array)
# 집합(set) 자료형은 크게 2가지 특징을 가지고 있다.
# 1) 중복을 허용하지 않는다.
# 2) 순서가 없다.

array = list(set_array)
array.sort()
array.sort(key = len)
# sort() 함수는 정렬 기준이 동일한 경우에 원래의 순서를 유지하는 안정 정렬 알고리즘을 사용한다.

print(*array)
