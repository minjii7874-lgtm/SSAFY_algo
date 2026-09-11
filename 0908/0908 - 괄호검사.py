T = int(input())

for tc in range(1, T + 1):
    # 검사할 코드 입력
    code = input()

    # 괄호검사에 사용할 스택
    stack = []

    pair = {"{": "}", "(": ")"}

    # 문제에서 원하는 답 -> 괄호가 제대로 되어 있는가
    # 일단 제대로 되어 있다고 가정하고, 제대로 안된 조건 발견시 바꿔주면 됨
    answer = 1

    for c in code:
        # 검사할 코드에서 한글자 가져와서 c 라고 하자
        # c가 괄호인 경우만 신경쓰면 됨

        # 여는 괄호를 만나면 스택에 저장
        if c in "{(":
            stack.append(c)

        # 닫는 괄호를 만나면 스택에서 가장 최근에 저장한 괄호 하나 꺼내서
        # 모양 맞는지 확인
        if c in "})":
            # 스택에 꺼낸 괄호가 남아있는지 확인
            # 남아있지 않다면 ?? 오른쪽괄호(닫는괄호)의 개수가 더 많은 상황
            if not stack:
                answer = 0
                break

            # 스택에서 괄호 하나 꺼낸 후 짝이 맞는지 모양 검사
            left = stack.pop()
            if pair[left] != c:
                # c=현재 내가 보고 있는 오른쪽(닫는) 괄호
                # left = 스택에서 꺼낸 왼쪽(여는) 괄호
                answer = 0
                break

    # 코드를 다 확인하고 나서 스택에 왼쪽 괄호가 남아있다면
    # 왼쪽 괄호의 개수가 오른쪽 괄호의 개수보다 많은 상황
    if stack:
        answer = 0

    print(f"#{tc} {answer}")
