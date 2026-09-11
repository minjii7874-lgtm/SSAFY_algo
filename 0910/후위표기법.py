# 중위표기법(infix) -> 후휘표기법(postfix)

# 스택 외부(icp) 우선순위
icp = {"(": 3, "*": 2, "/": 2, "+": 1, "-": 1}
# 스택 내부(isp) 우선순위
isp = {"(": 0, "*": 2, "/": 2, "+": 1, "-": 1}


# 중위표기식 -> 후위표기식
def get_postfix(infix, n):
    # 결과로 출력할 후위표기식
    postfix = ""

    # 연산자를 저장할 스택
    stack = []

    # "(6+5*(4/2))"

    for i in range(n):
        # 중위표기식의 i번째 토큰 가져와서
        # 피연산자 ? 연산자?
        if infix[i] not in "()+-*/":
            # 피연산자라면 출력(후위표기식)에 그대로 써주기
            postfix += infix[i]
        else:
            # 연산자
            # 오른쪽 괄호인 경우:
            # 스택 안에 있는 연산자를 모두 꺼내서 출력
            # 왼쪽 괄호를 꺼낼때까지
            if infix[i] == ")":
                while stack:
                    # 연산자를 하나 꺼내서
                    op = stack.pop()
                    # 왼쪽 괄호이면 꺼내기 중단
                    if op == "(":
                        break
                    # 아니면 출력에 써주기
                    postfix += op

            else:
                # 스택에서 연산자를 꺼내는 상황부터 체크
                # 현재 우리가 보고 있는 연산자 infix[i]
                # 보다 우선순위가 낮거나 높은 연산자가 스택에 있는 경우
                # infix[i] 의 우선순위 <= stack의 꼭대기 연산자의 우선순위

                # 스택 안에 연산자의 우선순위가 높으므로 먼저 계산되어야 한다.
                while stack and icp[infix[i]] <= isp[stack[-1]]:
                    # 스택 안의 연산자 꺼내서 출력
                    postfix += stack.pop()

                # 스택이 비었다. or 스택 꼭대기의 연산자가 infix[i]보다 우선순위가 낮다.
                stack.append(infix[i])

    # 스택에 남아있는 연산자 모두 꺼내서 출력
    # 우선순위가 낮은 연산자들 모두 출력
    while stack:
        postfix += stack.pop()

    return postfix


infix = "(6+5*(2-8)/2)"
postfix = get_postfix(infix, len(infix))
print(postfix)




# 후위표기식의 결과값 계산
def get_result(postfix):
    stack = []

    for c in postfix:
        # c가 피연산자(숫자)? 연산자?
        if c not in "+-*/":
            # 타입 조심
            stack.append(int(c))
        else:
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
                result = s / e

            # 이 계산 결과를 다른 연산자가 사용
            stack.append(result)


    # 계산이 완료되면 스택에 숫자 하나 남음 -> 최종 결과값
    return stack.pop()

result = get_result(postfix)
print(result)
