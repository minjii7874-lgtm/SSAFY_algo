N = int(input())

boxes=list(map(int, input().split()))

for i in range(N):
    count = 0

    for j in range( i+1 , N):
        if boxes[i] > boxes[j]:
            