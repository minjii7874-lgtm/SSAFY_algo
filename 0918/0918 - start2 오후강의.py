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