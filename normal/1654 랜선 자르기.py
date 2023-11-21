def binary_search(lans):
    pl = 1
    pr = lans
    
    while pl <= pr:
        pc = (pl+pr) // 2
        buff = 0

        for i in a:
            buff += i // pc

        if buff < n:
            pr = pc-1
        else:
            pl = pc+1

    return pr

k, n = map(int, input().split())
a = []
            
for _ in range(k):
    lan = int(input())
    a.append(lan)

print(binary_search(sum(a) // n))
