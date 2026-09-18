T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    answer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0

    while answer:

        count += 1

        num = N * count

        for i in str(num):

            if int(i) in answer:
                answer.remove(int(i))

    print(f"#{tc} {count}")