n = int(input())

for i in range(1, n+1):
    i_sum = sum(map(int, str(i)))
        
    if i + i_sum  == n:
        print(i)
        break
else:
    print(0)
