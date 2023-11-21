n, b = input().split()
n = n[::-1] # 시퀀스 자료형은 인덱스를 통해 접근할 수 있다.
b = int(b)
result = 0

for i in range(len(n)):
    if n[i].isdigit():
        # isdigit() 함수는 문자열이 숫자로만 이루어져 있는지 확인하는 함수이다.
        # 음수를 뜻하는 '-', 소수점을 뜻하는 '.' 등을 문자로 판단하기에 실수나 음수를 판단할 수 없다.
        result += int(n[i]) * (b ** i)
    else:
        result += (ord(n[i]) - 55) * (b ** i)
        
print(result)
