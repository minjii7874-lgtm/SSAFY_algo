T = int(input())

for tc in range(1, T + 1):
    # 작은 문자열
    str1 = input()
    # 큰 문자열
    str2 = input()

    # N: 작은 문자열의 길이, M: 긴 문자열의 길이
    N, M = len(str1), len(str2)

    # 문제에서 원하는 답 : 큰 문자열 안에 작은 문자열이 존재하는지 여부 1(있다) or 0(없다)
    answer = 0

    # 비교를 시작하는 긴 문자열의 기준 인덱스 i
    for i in range(M-N+1):
        # 작은 문자열의 인덱스 j ( 0~N-1)
        # j는 또한 기준 인덱스(i)에서 몇 칸 떨어져있는지 나타내는 값 이기도 함
        # 작은 문자열에 j번 인덱스와 비교해야할 큰 문자열의 인덱스 번호는 (i+j)번
        for j in range(N):
            # 큰 문자열[i+j] != 작은 문자열 [j]
            if str2[i+j] != str1[j]:
                # 중간에 다른 부분을 발견했으면 이 뒤는 볼 필요 없음
                break

        # 중간에 반복문이 break 된 적 없으면 실행되는 코드(for-else)
        else:
            # j번 반복하면서 다른 부분이 없었다. -> 일치하는 문자열 발견!
            answer = 1

    print(f"#{tc} {answer}")