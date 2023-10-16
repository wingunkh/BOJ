def divisor(n):
    a = []
    
    for i in range(1, n):
        if n % i == 0:
            a.append(i)

    return a

while True:
    n = int(input())
    
    if n == -1:
        break
    
    a = divisor(n)
    
    if sum(a) == n:
        print(f"{n} =", " + ".join(str(i) for i in a))
    else:
        print(f"{n} is NOT perfect.")
