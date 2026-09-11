# i번 행에서 j번 열을 골라서 합을 만들자
# j 는 중복 불가
# 0번행 -> 0번열
# 1번행 -> 1번열 (이전에 사용했던 열 번호는 사용 불가)
# ...
# N-1번행 -> N-1번열
# selected : 지금까지 고른 열번호 체크
# s : 지금까지 고른 숫자들의 합

def make_perm(i, selected, s):
    global answer

    # 0. 가지치기
    # 내가 지금까지 구한합 s가 이전에 구한 최소합 answer보다 같거나 크면
    # 더 이상 진행 할 필요가 없다
    if s >= answer:
        return

    # 1. 종료 조건
    # N개의 행에 대해서 어떤 열을 사용할지 각가 선택 완료
    if i == N:
        # 이 합이 최소인지 확인
        if s < answer:
            answer = s
        return

    # 2. 재귀 호출
    # 0~ N-1 열 중에서 하나 고르기, 단 이전에 골랐던 열번호는 불가능
    for j in range(N):
        if not selected[j]:
            selected[j] = 1
            # i번 행은 j열을 사용하고, 다음 i+1 행으로
            make_perm(i + 1, selected, s + matrix[i][j])
            # j열 말고 다른 열 번호를 쓸 것이기 때문에 원상복구 (쓴 적 없음으로 되돌림)
            selected[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 최소합
    answer = 100

    # 재귀호출
    # 0번 행부터 고르기 시작, 아무것도 고르지 않은 상태, 합은 0에서 시작
    make_perm(0, [0] *N, 0)


    print(f"#{tc} {answer}")
