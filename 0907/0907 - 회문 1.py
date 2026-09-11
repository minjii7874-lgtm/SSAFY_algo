T = 10

for tc in range(1,T+1):
    N = 8
    M = int(input())

    text= [input() for _ in range(N)]

    # 찾은 회문 개수
    answer = 0


    # 가로 회문
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if text[i][j+k] != text[i][j+M-1-k]:
                    break

            else:
                answer += 1

    # 세로 회문
    for j in range(N):
        for i in range(N-M+1):
            for k in range(M//2):
                if text[i+k][j] != text[i+M-1-k][j]:
                    break
            else:
                    answer += 1

    print(f"#{tc} {answer}")
