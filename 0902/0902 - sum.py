# import sys
# sys.stdin = open("sum_input.txt", "r")
# sys.stdout = open("sum_output.txt", "w")


T = 10

for tc in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0

    # 행의 합
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]

        if row_sum > max_sum:
            max_sum = row_sum

    # 열의 합
    for j in range(100):
        col_sum = 0

        for i in range(100):
            col_sum += arr[i][j]

        if col_sum > max_sum:
            max_sum = col_sum

    # 대각선의 합
    diagonal_1 = 0
    diagonal_2 = 0

    for i in range(100):
        diagonal_1 += arr[i][i]
        diagonal_2 += arr[i][99-i]

    if diagonal_1 > max_sum:
        max_sum = diagonal_1
    if diagonal_2 > max_sum:
        max_sum = diagonal_2

    print(f"#{tc} {max_sum}")