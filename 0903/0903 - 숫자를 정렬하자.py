# 버블정렬, 카운팅정렬 사용해서 각각 제출 하기

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    numbers = list(map(int, input().split()))

    ## 1.선택정렬
    for i in range(N-1):
        # i번 인덱스 자리 주인 찾기
        # 0번 -> 최소값
        # 1번 -> 그 다음 최소값
        # 2번 -> 그 다음다음 최소값

        #최소값의 위치(일단 i라고 가정)
        min_idx = i

        #i뒤에서부터 최소값을 찾기 시작
        for j in range(i+1, N):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        #최소값이 있는 위치, i위치에 있는 원소를 교환
        numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]

    print(f"#{tc}", *numbers)


##2. 버블정렬
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(N-1-i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


    print(f"#{tc}", *numbers)




##3. 카운팅정렬
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    count = [0] * N
    result = [0] * N

    for i in range(N):
        for j in range(N):
            if numbers[i] > numbers[j]:
                count[i] +=1

    for i in range(N):
        for j in range(i):
            if numbers[i] == numbers[j]:
                count[i] +=1

    for i in range(N):
        result[count[i]] = numbers[i]

    print(f"#{tc}", *result)