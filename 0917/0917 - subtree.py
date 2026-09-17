T = int(input())

for tc in range(1, T + 1):
    # E: 간선의 개수
    # N: 순회를 시작하는 노드의 번호(서브트리의 루트 노드 번호)
    E, N = map(int, input().split())

    # V:노드의 개수 = 간선의 개수 +1 개(E+1)
    V = E + 1

    left = [0] * (V + 1)
    right = [0] * (V + 1)

    # 간선 정보 입력
    tree = list(map(int, input().split()))

    for i in range(E):
        p = tree[i * 2]
        c = tree[i * 2 + 1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c


    count = 0

    def preorder(t):
        global count

        if t:
            # t번 노드에 도착할 때마다 노드 개수 +1
            count += 1
            preorder(left[t])
            preorder(right[t])

    # N번 노드부터 전위순회 시작
    preorder(N)

    print(f"#{tc} {count}")

