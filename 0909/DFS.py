# 인접 행렬
# A=0, B=1 ... G=6
# 정점의 개수 N = 7개

# adj_matrix=[]
# 1번정점과 2번정점이 인접해있다.
# adj_matrix[1][2] = 1
# adj_matrix[2][1] = 1 (단, 방향이 있는 그래프라면 0일수도 있다.)
# 3번정점과 4번정점이 인접해있지 않다
# adj_matrix[3][4] = 0
# adj_matrix[4][3] = 0


# V : 정점의 개수 , E : 간선의 개수
V, E = map(int, input().split())
#  그래프의 연결 정보가 한줄로 입력됨
G = list(map(int, input().split()))

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    s = G[2 * i]
    e = G[2 * i + 1]
    adj_matrix[s][e] = 1
    adj_matrix[e][s] = 1

# print(*adj_matrix, sep="\n")

"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

print()

adj_list = [[] for _ in range(V + 1)]
# adj_list[4] = [1,2,3] : 4번 정점과 1,2,3 정점이 인접해있다
# adj_list[2] = [] : 2번 정점과 연결된 정점이 없다
for i in range(E):
    s = G[2 * i]
    e = G[2 * i + 1]
    adj_list[s].append(e)
    adj_list[e].append(s)


# print(*adj_list, sep="\n")


# s : 탐색 시작 정점 번호
# V : 정점의 개수

def dfs(s, V):
    # DFS: 깊이우선탐색, 그래프의 모든 정점을 빠짐없이 한번씩 모두 탐색
    visited = [0] * (V + 1)
    # visited[5]=1 :5번 정점은 이전에 방문한적이 있다.
    # visited[4]=0 :4번 정점은 이전에 방문한적이 없다.

    # 돌아올 곳을 기억(저장)할 스택
    stack = []

    visited[s] = -1
    # 현재 내가 위치한 정점 번호 v
    v = s
    print(v)

    # 그래프 탐색 시작
    while True:
        # 현재 내가 있는 정점 번호 v
        # v와 인접한 정점 중에 간적이 없느 정점 w를 찾는다.
        # 돌아올 정점번호 v를 스택에 저장하고, w를 새로운 v로 저장해서 탐색을 반복

        for w in range(V + 1):
            # v와 w가 인접해있고 w를 방문한 적이 없다면
            if adj_matrix[v][w] and not visited[w]:
                # v를 스택에 저장하고, w로 바로 이동
                stack.append(v)
                visited[w] = 1
                print(w)
                v = w
                # 새로 바뀐 v에서 연결된 정점을 찾아야 하므로 break
                break
        else:
            # 반복문에서 break되지 않았다면 -> 이동할 수 있는 w를 찾지 못함, 갈 길이 없음
            # 이전 정점으로 되돌아가서 새로운 길이 찾아야 한다 -> stack.pop() 하면 가장 최근에 방문한
            # 정점 번호를 알아낼 수 있다
            if stack:
                v=stack.pop()
            else:
                #while break
                # 스택에 더이상 돌아갈 정점이 남아있지 않다면 모든 정점을 다 방문했다
                break

dfs(1,7)




def dfs2(s,V):
    # DFS: 깊이우선탐색, 그래프의 모든 정점을 빠짐없이 한번씩 모두 탐색
    visited = [0] * (V + 1)
    # visited[5]=1 :5번 정점은 이전에 방문한적이 있다.
    # visited[4]=0 :4번 정점은 이전에 방문한적이 없다.

    # 돌아올 곳을 기억(저장)할 스택
    stack = []

    visited[s] = -1
    # 현재 내가 위치한 정점 번호 v
    v = s
    print(v)

    # 그래프 탐색 시작
    while True:
        # 현재 내가 있는 정점 번호 v
        # v와 인접한 정점 중에 간적이 없느 정점 w를 찾는다.
        # 돌아올 정점번호 v를 스택에 저장하고, w를 새로운 v로 저장해서 탐색을 반복


        #인접리스트는 연결되어있는 정점 번호만 저장
        #adj_list[v] : v와 인접한 정점 번호 리스트
        for w in adj_list[v]:
            # v와 w가 인접해있고 w를 방문한 적이 없다면
            if not visited[w]:
                # v를 스택에 저장하고, w로 바로 이동
                stack.append(v)
                visited[w] = 1
                print(w)
                v = w
                # 새로 바뀐 v에서 연결된 정점을 찾아야 하므로 break
                break
        else:
            # 반복문에서 break되지 않았다면 -> 이동할 수 있는 w를 찾지 못함, 갈 길이 없음
            # 이전 정점으로 되돌아가서 새로운 길이 찾아야 한다 -> stack.pop() 하면 가장 최근에 방문한
            # 정점 번호를 알아낼 수 있다
            if stack:
                v = stack.pop()
            else:
                # while break
                # 스택에 더이상 돌아갈 정점이 남아있지 않다면 모든 정점을 다 방문했다
                break


dfs2(1, 7)
