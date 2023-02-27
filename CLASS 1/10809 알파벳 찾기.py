s = input()
alphabet = list(range(97, 123))

for i in alphabet :
    print(s.find(chr(i)), end = ' ')

# chr() 함수는 아스키코드를 문자로 변환하는 함수이다.
# find() 함수는 문자열에서 전달받은 문자나 문자열을 처음 발견한 인덱스를 반환한다.
