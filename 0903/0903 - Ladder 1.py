T = int(input())

for tc in range(1, T + 1):
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착점 2 찾기
    for j in range(100):
        if ladder[99][j] == 2:
            x = 99
            y = j
            break

    while x > 0:
        # 왼쪽에 길이 있을 때
        if y > 0 and ladder[x][y - 1] == 1:
            while y > 0 and ladder[x][y - 1] == 1: #왼쪽 길로 계속
                y -= 1

        # 오른쪽에 길이 있을 때
        elif y < 99 and ladder[x][y + 1] == 1:
            while y < 99 and ladder[x][y + 1] == 1: #오른쪽 길로 계속
                y += 1

        else:
            x -= 1
    print(f"#{tc} {y}")
