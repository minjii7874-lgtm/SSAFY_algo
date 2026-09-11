T = int(input())

for tc in range(1, T+1):
    N, M = map(int, (input().split()))

    # N*M 문자열 정보 입력
    text = [input() for _ in range(N)]

    # 우리가 찾아낸 회문
    answer = ""

# 회문 찾기

# 행 번호 i
    for i in range(N):
    # 열 번호 j, 가로 방향 회문 찾기, j에서 회문을 만들기 시작할 때 j+m 이 N보다 크면 안됨.
        for j in range(N-M+1):
        # (i,j) 에서 가로 방향 회문 찾기
        # (i,j) ~ (i, j+M)
        # M//2 만큼 비교, 비교 횟수 k
            for k in range(M//2):
                if text[i][j+k] != text[i][j+M-1-k]:
                    break

        # for문 break 된 적이 없으면 회문 발견
            else:
                answer = text[i][j:j+M]
                break

        # 세로 방향 판별 => 행번호 j, 열번호 i라고 하면 해결
            for k in range(M//2):
                if text[j+k][i] != text[j+M-1-k][i]:
                    break
            else:
                for l in range(M):
                    answer += text[j+l][i]


    print(f'#{tc} {answer}')