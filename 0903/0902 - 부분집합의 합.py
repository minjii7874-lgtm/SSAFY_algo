T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # 1부터 12까지의 숫자를 가진 집합

    # 부분집합의 개수
    count = 0

    # 모든 부분집합 확인 (<<비트연산자)
    for i in range(1 << len(A)):
        cnt = 0  # 부분집합 안에 들어있는 원소 개수
        total = 0  # 부분집합 안에 들어있는 원소들의 합

        for j in range(len(A)):
            if i & (1 << j):
                cnt += 1
                total += A[j]

        if cnt == N and total == K:
            count += 1

    print(f"#{tc} {count}")

# ================================
# 강사님
T = int(input())

# 모든 테스트 케이스 고정
arr = [i for i in range(1, 13)]  # 1~12
N = 12

for tc in range(1, T + 1):
    # n : 부분집합 원소의 개수
    # k : 부분집합의 합
    n, K = map(int, input().split())

    # 문제에서 원하는 답
    # 부분집합의 원소의 개수가 n개, 그 합이 k인 경우의 수
    answer = 0

    # 모든 부분집합의 개수는 1 << N 개
    # i : 부분집합 번호
    for i in range(1 << N):
        # i번 부분집합이 원소가 n개이고 합이 k 인지 확인
        ith_cnt = 0
        ith_sum = 0

        # i를 비트연산을 통해 부분집합 코드를 해독
        # i를 이진수로 생각하고 각 자리에 1과 & 연산을 통해 그 결과가 1인지 0인지 확인
        # 1-> 자릿수에 1이 있음. (그 인덱스에 있는 원소가 부분집합에 포함)
        # 0-> 자릿수에 0이 있음 (그 인덱스에 있는 원소가 부분집합에 미포함)
        # 실제 비트연산 결과로 나오는 숫자는 1이 아님에 주의!!

        #   1 0 0 1 0
        # & 0 0 1 0 0
        # ===========
        # => 2^2 = 4
        for j in range(N):
            if i & (1 << j):
                # j번 인덱스의 숫자는 i번 부분집합에 포함되어 있다!
                ith_sum += arr[j]
                ith_cnt += 1

        # i번 부분집합의 합이 K이고 원소의 개수가 n개인지 확인
        if ith_sum == K and ith_cnt == n:
            answer += 1

    print(f"#{tc} {answer}")
