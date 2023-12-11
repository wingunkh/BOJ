import sys
input = sys.stdin.readline

def append_star(n):
    if n == 1:
        return '*'

    stars = append_star(n // 3) 
    result = []  
    
    for s in stars:
        result.append(s * 3)
        
    for s in stars:
        result.append(s + ' ' * (n // 3) + s)
        
    for s in stars:
        result.append(s * 3)
        
    return result

n = int(input())

print(*append_star(n), sep = '\n')
