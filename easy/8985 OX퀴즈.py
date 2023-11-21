n = int(input())

for _ in range(n):
    a = input()
    result = 0
    score = 1

    for i in a:
        if i == 'O':
            result += score
            score += 1
        else:
            score = 1
            
    print(result)
