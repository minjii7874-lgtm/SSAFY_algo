T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T + 1):
    # N = 행의 개수, M = 열의 개수
    N, M = map(int, input().split())

    # 꽃가루 개수가 들어있는 2차원 리스트 입력
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 답(꽃가루 합의 최대값)
    answer = 0

    # 모든 위치에서 풍선 다 터뜨려보기
    for i in range(N):
        for j in range(M):
            # (i,j) 위치에서 풍선 터뜨린 후 꽃가루 개수만큼 상하좌우 +
            # 이 위치에서 꽃가루 합
            cnt = arr[i][j]

            # 상하좌우로 뻗어나갈 길이 k의 범위는 (i,j) 위치의 꽃가루 개수만큼
            for k in range(1, cnt + 1):
                # 상하좌우 4방향 델타 탐색
                for d in range(4):
                    # d 방향으로 k 만큼 뻗어나간 위치 (ni ,nj)
                    ni = i + di[d] * k
                    nj = j + dj[d] * k
                    # 계산한 다음 위치가 인덱스 범위 안인지 확인
                    if 0 <= ni < N and 0 <= nj < M:
                        # 유효한 위치라면 꽃가루 개수 + 해주기
                        cnt += arr[ni][nj]

            # 최대값 갱신
            answer = max(answer, cnt)

    print(f"#{tc} {answer}")