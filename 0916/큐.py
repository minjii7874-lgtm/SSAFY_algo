# front 와 rear를 사용하는 방법

# 큐의 크기
N = 10
# 공백상태의 큐를 생성
q = [0] * N
# front : 마지막에 삭제된 원소의 위치( +1 하면 첫 원소의 위치)
# rear : 마지막 원소의 위치
front = rear = -1

for i in range(1,11):
    # 삽입 할 때는 rear 만 보면 됨
    rear += 1
    q[rear] =i

print(q)
print(front, rear)

for i in range(10):
    # 삭제를 할 때는 front만 보면 됨
    front +=1
    print(q[front], end=" ")
print()

print(q)
print(front, rear)
