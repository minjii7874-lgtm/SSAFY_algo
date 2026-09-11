# 파이썬의 리스트 메서드를 사용한 방법

# 스택 초기화
# 스택으로 사용할 리스트 선언
stack = []

# 스택에 자료를 추가(push)
for i in range(1,11):
    stack.append(i)

print(stack)

# stack이라는 변수는 "스택"이라는 자료구조를 사용할 것이기 때문에
# 아래 코드는 사용하지 않는다.
# stack[2] =16

# 스택에서 자료를 삭제(pop)
# for i in range(10):
#     e = stack.pop()
#     print(e, end= " ")
# print()
#
# print(stack)

# 스택 안에 있는 자료 모두 삭제
while stack :
    e=stack.pop()
    print(e, end=" ")
print()

print(stack)

