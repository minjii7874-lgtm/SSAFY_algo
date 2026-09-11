T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    char = list(map(int, input().split()))

    current = 0
    count = 0

    while current + K < N:
        next_stop = current

        for stop in char:
            if current < stop <= current + K:
                if stop > next_stop:
                    next_stop = stop

        if next_stop == current:
            count = 0
            break

        current = next_stop
        count += 1

    print(f"#{tc} {count}")
