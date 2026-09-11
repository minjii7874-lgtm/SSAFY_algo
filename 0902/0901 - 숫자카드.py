T =int(input())

for tc in range(1, T+1):
    N=int(input())

    numbers=input()

    counts = [0] * 10

    for num in numbers:
        counts[int(num)]+=1

    max_count = max(counts)

    max_num = 0

    for n in range(10):
        if counts[n] == max_count:
            max_num = n


    print(f"#{tc} {max_num} {max_count}")


