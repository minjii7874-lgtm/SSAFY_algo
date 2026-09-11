#top 을 사용한 스택

# 스택의 크기
N =10
#top: 스택에서 꼭대기에 저장된 자료의 위치 (빈 상태에서는 -1)
# 마지막에 삽입된 자료의 위치 (인덱스)
top = -1
# 스택 초기화
stack = [0] * N

# 스택에 자료를 추가하기 (push)
for i in range(1,11):
    #N개 초과 불가능
    if top == N -1:
        print("overflow")
        break
    else:
        top +=1
        stack[top] = i

print(stack, top)

# 스택에서 자료 삭제하기 (pop)
for i in range(10):
    if top > -1:
        e=stack[top]
        top -=1
        print(e, end=" ")
    else:
        print("underflow")
        break
print()

print(stack, top)

top +=1
stack[top] = 100

print(stack, top)