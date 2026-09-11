T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    v = list(map(int, input().split()))

    sums =[]
    for i in range(N-M+1):
        total = sum(v[i:i+M])
        sums.append(total)

    answer = max(sums)-min(sums)

    print(f"#{tc} {answer}")