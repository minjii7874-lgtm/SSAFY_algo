T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    grid = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                grid[i][j] += color

    purple = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 3:
                purple += 1

    print(f"#{tc} {purple}")



# 강사님
T = int(input())


for tc n range(1, T + 1):
    N = int(input())


    paper = [[0] * 10 for _ in range(10)]

    # 보라색 칸의 개수
    purple = 0

    for _ in range(N):
        # 색칠 정보 입력 받기 (색칠시작 행번호, 열번호, 색칠마지막 행번호, 열번호, 색번호)
        i1, ji, i2, j2, color = list(map(int, input().split()))
    #(i1,j1)~(i2,j2)
    for i in range(i1, i2 +1):
        for j in range(j1, j2+1):
            # 0 : 흰색
            # 1 : 빨강
            # 2 : 파랑
            # 3 : 보라 (1+2)(빨강 + 파랑)
            paper[i][j] +=color

            if paper[i][j] ==3:
                purple +=1

    print(f"#{tc} {purple}")