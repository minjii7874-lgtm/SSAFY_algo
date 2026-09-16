from collections import deque
"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 

"""
# 정점의 개수 = V
# 간선의 개수 = E
V, E = map(int, input().split())

# 인접 행렬
adj_m = [[0] * (V + 1) for _ in range(V + 1)]

# 그래프 정보가 한줄로 들어옴
g = list(map(int, input().split()))

# 한줄로 들어온 그래프 정보를 간선의 개수만큼 2개씩 자름
for i in range(E):
    s, e = g[i * 2], g[i * 2 + 1]

    adj_m[s][e] = 1
    adj_m[e][s] = 1

# v : 탐색 시작 정점 번호
def bfs(v):
    # 중복 체크 배열
    # 중복 방문 체크 + 거리 계산
    visited =[0] * (V+1)

    # 큐
    # 내가 다음에 방문할 곳을 저장(예약), 꺼낸 순서대로 방문
    # 꺼내지는 순서는 먼저 들어간 자료가 나오게 됨

    # 시작 정점을 큐에 넣은 상태로 시작
    q = deque([v])
    visited[v] = 1

    # 큐 안에 방문할 곳이 남아있다면, 탐색 반복
    # 큐가 비었다 -> 더이상 방문할 곳이 없다 -> 탐색 완료
    while q:
        # 방문할 정점을 큐에서 꺼낸다
        t = q.popleft()
        # t정점에서 할일 처리
        print(t,end=" ")

        # t와 인접한 정점 탐색, 갈 수 있는 정점은 큐에 저장
        for n in range(1, V+1):
            # t에서 n정점이 인접해있고, n정점을 방문한 적이 없다면
            if adj_m[t][n] == 1 and not visited[n]:
                # n정점은 다음에 방문 예약
                q.append(n)
                # n정점 방문 했다고 표시
                # visited[n] = 시작지점에서 n번 정점까지의 최단거리
                # n과 t가 인접 -> 간선 하나로 연결이 되어 있음. 간선 하나 = 거리1
                # visited[n] = 시작지점에서 t번 정점까지의 최단거리 + 1
                visited[n] = visited[t] + 1


print(bfs(1))
