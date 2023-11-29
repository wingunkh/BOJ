# n개의 원판을 시작 막대에서 목표 막대로 옮기는 함수
def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    # 1단계: n-1개의 원판을 시작 막대에서 중간 막대로 옮긴다.
    hanoi(n-1, start, 6 - start - end)
    # 2단계: 남은 1개의 원판을 시작 막대에서 목표 막대로 옮긴다. 
    print(start, end)
    # 3단계: n-1개의 원판을 중간 막대에서 목표 막대로 옮긴다.
    hanoi(n-1, 6 - start - end, end)

n = int(input())

print(2 ** n - 1)
hanoi(n, 1, 3)
