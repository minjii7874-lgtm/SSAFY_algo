# 파이썬의 리스트 매서드 사용

# 공백상태의 큐 생성
q = []

for i in range(1,11):
    q.append(i)

print(q)

for i in range(10):
    e =q.pop(0)
    print(e, end =" ")
print()

print(q)
