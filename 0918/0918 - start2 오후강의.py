# 10진수 17을 3진수로 바꾸기

a = 17
trans = ""
while a != 0:
    rest = a % 3
    trans += str(rest)
    a //= 3

answer = trans[::-1]
print(answer)

result = int(answer, 3)
print(result)




arr=[1,2,3]
for i in range(1<<3):
    result=[]
    for index in range(3):
        if i&(1<<index)!=0:
            result.append(arr[index])
    print(result)




# 컴퓨터는 이진수를 사용하기 때문에 정확한 실수 표현이 불가능한 경우가 있다!!!

from decimal import Decimal
a =Decimal('1.2')-Decimal('1.1')
print(a)

a=1.2-1.1
print(a)

a=1.25
print(f'{a:.1f}')
a=1.35
print(f'{a:.1f}')
# 파이썬은 반올림을 가까운 짝수 쪽으로 한다...
print(round(4.5))
print(round(5.5))


# 1.25를 정확하게 표현하고 싶다
# 1.25 ->'1.25' -> .빼버리기 -> 10으로 나누기
a=1.25
a=str(a)
a=int(a.replace(".",''))
a=((a+5)//10)
print(f'{a//10}.{a%10}')