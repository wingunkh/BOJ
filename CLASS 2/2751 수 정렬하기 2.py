import sys

def merge_sort(a: list, left: int, right: int) -> None:
    if left < right:
        center = (left + right) // 2

        merge_sort(a, left, center) # 배열 앞부분을 병합 정렬
        merge_sort(a, center + 1, right) # 배열 뒷부분을 병합 정렬

        p = j = 0 # 배열 buff의 커서
        i = k = left # 배열 a의 커서

        while i <= center: # 배열 a의 앞부분을 배열 buff로 복사
            buff[p] = a[i]
            p += 1
            i += 1

        while i <= right and j < p: # 배열 a의 뒷부분과 배열 buff를 배열 a에 병합
            if buff[j] <= a[i]:
                a[k] = buff[j]
                j += 1
            else:
                a[k] = a[i]
                i += 1
            k += 1

        while j < p: # 배열 buff의 나머지 원소를 배열 a에 복사
            a[k] = buff[j]
            k += 1
            j += 1
        
n = int(input())
array = [None] * n
buff = [None] * n

for i in range(n):
    array[i] = int(sys.stdin.readline().strip())
    
merge_sort(array, 0, len(array) - 1)
del buff

print(*array, sep = "\n")
