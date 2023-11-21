n = int(input())

for _ in range(n):
    r, s = input().split()
    
    for i in s:
        print(i * int(r), end = '')
        
    print()
