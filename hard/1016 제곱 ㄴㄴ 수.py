min, max = map(int, input().split())
square = [i**2 for i in range(2, int(max ** 0.5)+1)] # max보다 작거나 같은 모든 제곱 수
result = [1 for _ in range(max-min+1)]

for i in square: # 제곱 수를 하나씩 가져와서 반복
    x = min // i * i

    while x <= max:
        if x >= min:
            result[x-min] = 0 # 제곱 수의 배수를 정답 리스트에서 제거
        x += i

print(sum(result))
