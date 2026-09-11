T = int(input())


def dfs(i, j, N):
    # 방문 체크 배열도 N*N 형태로
    visited = [[0] * N for _ in range(N)]

    # 상하좌우 델타배열
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    stack = []
    visited[i][j] = 1

    while True:
        # 3인 곳에 도착하면 바로 종료
        if maze[i][j] == 3:
            return 1
        # (i,j) 위치에 있는 노드의 4방향(상하좌우) 탐색 후
        # 2차원 리스트 범위 안이전에 방문하지 않았고, 벽이 아니여야 하고
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and maze[ni][nj] != 1:
                visited[ni][nj] =1
                stack.append((i, j))
                i, j = ni, nj
                break
        else:
            if stack:
                i, j = stack.pop()
            else:
                break

    # 반복문이 정상적으로 종료 -> 그래프의 모든 지점을 탐색했으나 3을 찾지 못함
    # 출구 없음
    return 0


for tc in range(1, T + 1):
    # 미로의 크기
    N = int(input())
    # 미로 정보 (2차원 리스트, 그래프)
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작지점 2 찾기
    si, sj = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
                break

    answer = dfs(si, sj, N)
    print(f"#{tc} {answer}")
