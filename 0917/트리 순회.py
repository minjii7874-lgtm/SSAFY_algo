# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 6 5 9 6 10 6 11 7 12 11 13

# 노드 개수(N번까지 있다)
N = int(input())

# 트리 정보가 한줄로 들어온다.
tree =list(map(int,input().split()))

left =[0] * (N+1)
right = [0] * (N+1)

# 간선의 개수는 N-1개
for i in range(N-1):
    # 부모 노드 번호
    p = tree[2*i]
    # 자식 노드 번호
    c = tree[2*i+1]

    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c


print(left)
print(right)


# 1. 전위순회 (VLR)
def preorder(t):
    # t번 노드가 존재하면
    if t:
        # t번 노드(V) 에서 할일 처리
        print(t,end=" ")
        # t번 노드의 왼쪽 자식(L) 처리
        preorder(left[t])
        # t번 노드의 오른쪽 자식(R) 처리
        preorder(right[t])


# 2. 중위순회(LVR)
def inorder(t):
    # t번 노드가 존재하면
    if t:
        # t번 노드의 왼쪽 자식(L) 처리
        inorder(left[t])
        # t번 노드(V) 에서 할일 처리
        print(t,end=" ")
        # t번 노드의 오른쪽 자식(R) 처리
        inorder(right[t])


# 3. 후위순회(LRV)
def postorder(t):
    # t번 노드가 존재하면
    if t:

        # t번 노드의 왼쪽 자식(L) 처리
        postorder(left[t])
        # t번 노드의 오른쪽 자식(R) 처리
        postorder(right[t])
        # t번 노드(V) 에서 할일 처리
        print(t, end=" ")

preorder(3)
print()
inorder(1)
print()
postorder(1)



