for tc in range(1, 11):
    num, E = map(int, input().split())
    edges = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]

    for i in range(E):
        s = edges[2 * i]
        e = edges[2 * i + 1]
        adj_list[s].append(e)  # 방향 그래프이므로 한쪽 방향만 추가


    def dfs(s, target):
        visited = [0] * 100 # 모두 탐색
        stack = [] # 돌아올 곳을 기억할 스택
        visited[s] = -1
        v = s

        while True:
            for w in adj_list[v]:
                if not visited[w]: #w를 방문한 적 없다면
                    stack.append(v) #v를 스택에 저장하고
                    visited[w] = 1
                    v = w
                    break
            else:
                if stack:
                    v = stack.pop() #갈 곳이 없으면 이전 위치로 돌아감
                else:
                    break
        if visited[target]:
            return 1
        else:
            return 0


    result = dfs(0, 99)

    print(f"#{tc} {result}")
