import sys, math

a, b, v = map(int, sys.stdin.readline().split())

previous_day = math.ceil((v-a)/(a-b)) # ceil() 함수는 전달받은 값을 올림한 정수값을 반환한다.
print(previous_day + 1)
