# 2차원 리스트를 재귀함수로 순회하기
N = 5

matrix = [[N * i + j for j in range(1, N + 1)] for i in range(N)]

# 2차원 리스트 반복문 순회(행 우선 순회)
# i=0, j=0 -> i=0, j=1 ... i=0,j=4
# i=1, j=0 -> i=1, j=1 ... i=1,j=4
# ...
# i=4, j=0 -> i=4, j=1 ... i=4,j=4

for i in range(N):
    for j in range(N):
        print(matrix[i][j], end=" ")
    print()


# 재귀함수
# 반복문의 각 단계를 나타내는 파라미터 i,j 필요
def myprint(i,j):

    # 1. 종료조건 -> i,j 를 통해서 어떻게 나타낼 수 있는지, return
    if i==N:
        return
    # 2. 재귀호출 -> 현재 단계에서 필요한 작업을 수행한 후에 다음 단계 재귀호출
    print(matrix[i][j], end=" ")

    j += 1
    if j ==N:
        j=0
        i +=1
        print()

    myprint(i,j)
print("=======")
myprint(0,0)
#     if j == N-1:
#         print()
#         myprint(i+1, 0)
#
#     else:
#         myprint(i, j+1)
#
# myprint(0,0)