T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]


    answer = 0

    for i in range(N):
        for j in range(i, N):
            a, b= arr[i]
            c, d = arr[j]


            if (a > c and b <d) or (a <c and b>d):
                answer +=1

    print(f"#{tc} {answer}")