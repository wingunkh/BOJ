import sys
input = sys.stdin.readline

def binary_search(a: list, key: int) -> None:
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2

        if a[pc] == key:
            return dic.get(key)

        elif a[pc] < key:
            pl = pc + 1

        else:
            pr = pc - 1
            
        if pl > pr:
            return 0

n = int(input())
card = list(input().split())
card.sort()
m = int(input())
target = list(input().split())

dic = {}
for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
for i in target:
    print(binary_search(card, i), end = ' ')
