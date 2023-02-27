n = int(input())

for _ in range(n):
    array = input()
    score = 0
    total = 0
    for i in array:
        if i == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)
