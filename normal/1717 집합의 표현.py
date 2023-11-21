import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(a): # 특정 노드의 대표 노드를 검색하는 함수
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
        # 재귀 호출 간 거치는 모든 노드를 대표 노드와 직접 연결
        # 추후 노드와 관련된 find 연산 속도가 O(1)로 변경

def union(a, b): # 각 노드가 속한 집합을 1개로 합치는 함수
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a # 대표 노드를 연결

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    number, a, b = map(int, input().split())

    if number == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
