a = list(input())

for i in range(len(a)):
    maximum = i
    
    for j in range(i+1, len(a)):
        if a[j] > a[maximum]:
            maximum = j
    a[i], a[maximum] = a[maximum], a[i]

print(*a, sep = '')
