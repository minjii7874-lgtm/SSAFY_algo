T = int(input())

for tc in range(1, T + 1):
    A, B, C = map(int, input().split())

    answer = 0

    # A < B < C 가 되어야하므로 answer에 +1 더 해서 하나 더 먹도록 해야함
    if B >= C:
        answer +=B-C+1
        B = C-1

    if A >= B:
        answer += A-B+1
        A = B-1

    if A<=0 or B <=0:
        answer = -1

    print(f"#{tc} {answer}")