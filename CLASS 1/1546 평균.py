n = int(input())
array = list(map(int, input().split()))
max = max(array)

for i in range(len(array)):
    array[i] = array[i]/max*100

print(sum(array)/len(array))
