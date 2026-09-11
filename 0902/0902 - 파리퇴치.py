import sys
sys.stdin = open("input.txt", "r") #입력을 파일로
sys.stdout = open("output.txt", "w") #출력을 파일로

T = int(input())

for tc in range(1, T + 1):
    # 각 테스트 케이스마다
    # 영역의 크기 N과 파리채 크기 M이 주어진다.
    N, M = map(int, input().split())

    # 파리가 있는 영역, 파리 마리수가 2차원 리스트 입력
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 이 문제에서 구해야 하는 답
    # M*M 영역의 합 중 최대값 (파리채로 잡을 수 있는 파리의 최대값)
    answer = 0

    # 행번호 i
    # 파리채 크기를 고려해서 가능한 i 의 범위만 지정(전체 크기 - 파리채 크기)까지 가능
    for i in range(N-M+1):
        # 열번호 j
        # 파리채 크기를 고려해서 가능한 j 의 범위만 지정
        for j in range(N-M+1):
            # (i,j) 위치에서 M*M 크기의 사격형 범위 탐색
            # 작은 정사각형 내의 행번호 ni, 열번호 nj
            # 이 위치에서 파리채로 잡을 수 잇는 파리 마리 수
            fly = 0
            for ni in range(i, i+M):
                for nj in range(j, j+M):
                    # (ni,nj) 위치에 있는 파리수 알아내서 누적합 구하기
                    fly += arr[ni][nj]


            # M*M 영역의 합을 모두 구한 뒤에 최대값 갱신
            answer=max(fly, answer)


    # 파리채 다 만들어보고 나서 정답 출력
    print(f"#{tc} {answer}")
