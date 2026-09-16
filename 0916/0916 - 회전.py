from collections import deque

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = deque(map(int, input().split()))

    for i in range(M):
        arr.append((arr.popleft()))



    print(f"#{tc} {arr[0]}")
