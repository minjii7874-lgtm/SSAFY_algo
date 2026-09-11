T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    # 간선 정보 저장
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())

    visited = [False] * (V + 1)

    def dfs(node):
        # 도착점에 도착하면 경로 존재
        if node == G:
            return True

        visited[node] = True

        for next_node in graph[node]:
            if not visited[next_node]:
                if dfs(next_node):
                    return True

        return False

    if dfs(S):
        answer = 1
    else:
        answer = 0

    print(f"#{tc} {answer}")
