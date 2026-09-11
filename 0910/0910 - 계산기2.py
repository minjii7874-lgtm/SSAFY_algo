def get_postfix(infix,n):
    postfix=""

    stack=[]

    for i in range(n):
        if infix[i] not in "+*":
            postfix += infix[i]
        else:
            if infix[i] == "*": #우선순위 * 더 높으니까 먼저
                while stack and stack[-1] =="*": #스택이 비어있지 않고 맨 위에 *가 있을 때
                    postfix +=stack.pop()

                #while 문이 끝난 후 현재 * 넣음
                stack.append(infix[i])

            else: #"+"
                while stack:
                    postfix += stack.pop()

                #while 문이 끝난 후 현재 + 넣음
                stack.append(infix[i])

    #반복문이 끝난 후 남아 있는 연산자 처리
    while stack:
        postfix +=stack.pop()

    return postfix

def get_result(postfix):
    stack = []
 
    for c in postfix:
        if c not in "+*":
            stack.append(int(c))

        else:
            b = stack.pop()
            a = stack.pop()

            result = 0

            if c == "+":
                result = a + b
            elif c == "*":
                result = a * b

            stack.append(result)

    return stack.pop() # 스택에 하나 남은 숫자 = 최종 결과값

for tc in range(1, 11):
    N =int(input())
    susik = input()

    #중위표기식 -> 후위표기식
    postfix=get_postfix(susik,N)
    #후위표기식 계산
    result=get_result(postfix)
    print(f"#{tc} {result}")





