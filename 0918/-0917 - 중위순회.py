for tc in range(1, 11):

    N = int(input())

    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        data = input().split()

        node = int(data[0])
        tree[node] = data[1]

        # 자식이 1개인 경우
        if len(data) == 3:
            left[node] = int(data[2])

        # 자식이 2개인 경우
        elif len(data) == 4:
            left[node] = int(data[2])
            right[node] = int(data[3])

    def inorder(t):
        if t:
            inorder(left[t])
            print(tree[t], end="")
            inorder(right[t])

    print(f"#{tc}", end=" ")
    inorder(1)
    print()