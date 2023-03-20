n = int(input())
array = []
ranking = []

for i in range(n):
    x, y = map(int, input().split())
    array.append([x, y])

for i in range(n):
    count = 0
    for j in range(n):
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            count += 1
    ranking.append(count + 1)

print(*ranking)
