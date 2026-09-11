# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T + 1):
    # 테스트 케이스마다 숫자 입력 하나 처리
    num = int(input())


    # 카운트 배열
    # 각 자리의 숫자가 몇번 등장했는지 세어본다.
    counts = [0] * 12

    # 숫자에서 각 자리수 숫자 떼어내는 방법
    # //(몫) 랑 %(나머지) 연산자 사용하기


    for i in range(6):
        # 일의 자리 숫자 떼어내고
        counts[num % 10] += 1
        # 다음 자리수로 이동
        num = num // 10

    # run / triplet 확인할 기준 숫자
    i =0
    # babygin 조건 run 횟수 + tri 횟수 = 2
    tri = run_cnt =0

    while i < 10:

        # 트리플부터 확인
        # 숫자 i가 3번 이상 등장했다 -> 트리플
    if counts[i] >= 3:
        # 같은 숫자 3장 썼으니까 개수 차감
        counts[i] -= 3
        # 트리플 1회 발견
        tri += 1
        # 같은 숫자에서 트리플 최대 2번 발생 가능
        continue
    # 숫자 i에서 시작해서 i, i+1, i+2가 한 개 이상씩 존재한다 -> 런
    if counts[i] >=1 and counts[i+1] >=1 and counts[i+2]>=1:
        # i, i+1, i+2 숫자 한번씩 사용했으니까 개수 차감
        counts[i] -=1
        counts[i+1] -=1
        counts[i+2] -=1
        # 런 1회 발견
        run_cnt += 1
        # 같은 숫자에서 런 최대 2번 발생 가능,
        # i 가 증가하지 않도록 처리
        continue

    # run, triple 발견 못함 -> i 증가
    i += 1


    # 정답 출력은 i 반복 끝나고 나서서
    if tri + run_cnt == 2:
        print(f"#{test_case} Baby Gin")
    else:
        print(f"#{test_case} Lose")