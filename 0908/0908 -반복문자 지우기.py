T = int(input())

for tc in range(1, T+1):
    text = input()

    size = 1000
    top = -1
    stack = [0] * size


    for i in range(len(text)):
        # 스택이 비어있으면 비교할 글자가 없다 -> push
        if top == -1:
            top +=1
            stack[top] = text[i]
        # 스택에 비교할 글자가 있는 경우
        else:

            # i-1번 글자와 비교해서 다르면 -> push
            if stack[top] != text[i]:
                top += 1
                stack[top] = text[i]
            # i-1번 글자와 비교해서 같으면 -> pop
            else:
                top -=1

    # 스택에 남아있는 원소의 개수 = top +1
    print(f"#{tc} {top+1}")