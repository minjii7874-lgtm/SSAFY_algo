from collections import deque


for tc in range(1,11):
    T = int(input())
    num = list(map(int,input().split()))

    q=deque()

    for i in num:
        q.append(i)



    while True:
        for i in range(1,6):
            n = q.popleft()
            n -= i

            if n <= 0:
                n=0
                q.append(n)
                break

            q.append(n)
        if q[-1] ==0:
            break

    print(f"#{tc}", *q)