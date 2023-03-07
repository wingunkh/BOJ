n = int(input())

for i in range(n):
    i = str(i)
    sum = 0
    
    for j in i:
        sum += int(j)
        
    if int(i) + sum == n:
        print(i)
        break
else:
    print(0)
