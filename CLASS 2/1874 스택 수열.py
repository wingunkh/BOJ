class Stack:
    def __init__(self, capacity: int) -> None:
        self.stk = [None] * capacity # 스택 본체
        self.ptr = 0 # 스택 포인터(스택에 쌓여있는 데이터의 개수를 나타내는 정숫값)

    def push(self, value: int) -> None:
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> int:
        self.ptr -= 1
        return self.stk[self.ptr]

n = int(input())
input_array = [int(input()) for _ in range(n)]
output_array = []
s = Stack(n)
value = 1 # 푸시할 값

for i in input_array:
    while value <= i:
        s.push(value)
        output_array.append("+")
        value += 1
        
    if s.pop() == i:
        output_array.append("-")
    else:
        output_array.append("X")
        break

try:
    output_array.index("X")
    print("NO")
except:
    print(*output_array, sep = "\n")
