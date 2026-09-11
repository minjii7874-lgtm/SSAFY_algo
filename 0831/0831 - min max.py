T = int(input())

# tc는 테스트케이스 번호
for tc in range(1, T+1):
    # 테스트 케이스별 입력 처리

    # 테스크케이스별 숫자의 개수
    N = int(input())

    # 한줄 입력 받아서 숫자 리스트로 바꾸기
    numbers = list(map(int, (input().split())))

    # 최소값
    minv = numbers[0]
    # 최대값
    maxv = numbers[0]
    # 일단 맨 앞에 있는 원소를 최대값/최소값이라고 생각하고 시작

    # numbers에서 숫자 하나씩 꺼내서 비교해가며 최소값/최대값 구하기
    for num in numbers:
        if maxv < num:
            maxv = num

        if minv > num:
            minv = num

    # 테스트케이스별 정답 출력

    answer = maxv-minv
    print(f"{tc} {answer}")