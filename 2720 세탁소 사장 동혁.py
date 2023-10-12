t = int(input())

for _ in range(t):
    c = int(input())
    
    for i in [25, 10, 5, 1]:
        print(c // i, end = ' ')
        c = c % i
        
    print()
