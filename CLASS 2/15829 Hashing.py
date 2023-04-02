import sys
input = sys.stdin.readline

n = int(input())
string = input()
sum = 0

for i in range(n):
    sum += (ord(string[i]) - 96) * (31 ** i)
    
print(sum % 1234567891)
