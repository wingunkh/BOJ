import sys
input = sys.stdin.readline

n, m = map(int, input().split())
string_set = set([input() for _ in range(n)])
# 집합(Set)은 해시 테이블(Hash table)로 구현되어있다.
# 해시 테이블은 키(Key)에 데이터(Value)를 저장하는 데이터 구조이다. (예: 딕셔너리(Dictionary))
# 집합에서 각 요소는 해시 함수를 통해 해시 값으로 변환되며, 키 역할을 한다. (집합은 키만 존재한다.)
# 그러므로 집합에서의 in 연산의 시간복잡도는 O(1)이다.
answer = 0

for _ in range(m):
    if input() in string_set:
        answer += 1

print(answer)
