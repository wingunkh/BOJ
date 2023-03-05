class Queue:
    def __init__(self, capacity: int) -> None:
        self.rear = 0 # rear는 맨 끝 원소 바로 뒤의 인덱스(다음 인큐되는 데이터가 저장되는 위치)
        self.que = [None] * capacity # 큐의 본체
                 
    def enque(self, x: int) -> None:
        self.que[self.rear] = x
        self.rear += 1

    def deque(self, x: int) -> int:
        cnt = 0 # x가 몇 번째에 deque 되었는지 저장
        
        while (x != -1): # x가 -1이라면 deque 된 상태이므로 반복문 종료
            if self.que[0] == max(self.que):
                del self.que[0]
                x -= 1
                cnt += 1
            else:
                self.que.append(self.que[0])
                del self.que[0]
 
                if x == 0:
                    x = len(self.que) - 1
                else:
                    x -= 1
        return cnt
            
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    q = Queue(n)

    for i in p:
        q.enque(i)

    print(q.deque(m))
