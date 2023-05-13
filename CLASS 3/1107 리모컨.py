import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = list(map(int, input().split()))

minimum = abs(100 - N)

for i in range(1000001):
    i = str(i)
    
    for j in i:
        if int(j) in broken: # 고장난 버튼이 존재하는 경우, 해당 채널은 이동할 수 없음
            break
    else: # 고장난 버튼이 없는 경우, 해당 채널로 이동하기 위해 버튼을 누르는 횟수와 현재 채널로부터 N까지의 이동 횟수를 비교하여 최소값 갱신
        minimum = min(minimum, len(i) + abs(int(i) - N))

print(minimum)
