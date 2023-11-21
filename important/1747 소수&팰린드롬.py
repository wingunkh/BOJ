def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

n = int(input())
a = [i for i in range(10000001)]
a[1] = 0

for i in range(2, int(len(a) ** 0.5)+1):
    if a[i] == 0:
        continue
    
    for j in range(i+i, len(a), i):
        a[j] = 0

for i in range(n, len(a)):
    if a[i] == 0:
        continue

    if is_palindrome(i):
        print(i)
        break
