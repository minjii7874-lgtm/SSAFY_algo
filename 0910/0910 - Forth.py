T = int(input())
for tc in range(1, T+1):
    stack = []
    error = False
    answer = None
    for tok in input().split():
        if tok == '.':
            if len(stack) ==1:
                answer=stack.pop()
            else:
                error = True
            break
        elif tok == "+" or tok =="-" or tok =="*" or tok == "/":
            if len(stack) < 2:
                error = True
                break

            b=stack.pop() # 나중에 넣은 숫자
            a=stack.pop() # 먼저 넣은 숫자

            if tok == "+":
                result = a+b
            elif tok == "-":
                result = a-b
            elif tok == "*":
                result = a*b
            else:
                result = a//b


            stack.append(result)
        else:
            stack.append(int(tok))

    if error:
        print(f"#{tc} error")

    else:
        print(f"#{tc} {answer}")




"================="
# 강사님


T = int(input())

def get_result(postfix):
    stack = []

    for c in postfix[:-1]:
        # c가 피연산자(숫자)? 연산자?
        if c not in "+-*/":
            # 타입 조심
            stack.append(int(c))
        else:
            # c가 연산자라면 연산을 하기 위해서 피연산자 2개 필요
            if len(stack) < 2:
                return "error"

            # 뒤쪽 연산자
            e = stack.pop()
            # 앞쪽 연산자
            s = stack.pop()

            result = 0

            if c == "+":
                result = s + e
            elif c == "-":
                result = s - e
            elif c == "*":
                result = s * e
            elif c == "/":
                # 계산 결과 실수
                result = s // e

            # 이 계산 결과를 다른 연산자가 사용
            stack.append(result)


    # 계산이 완료되면 스택에 숫자 하나 남음 -> 최종 결과값
    if len(stack) > 1:
        return "error"
    else:
        return stack.pop()


for tc in range(1,T+1):
    susik = input().split()

    answer = get_result(susik)
    print(f"#{tc} {answer}")