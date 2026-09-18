decimal = 149

# 이진수로 바꾼 결과
print(bin(149))

binary = 0

# 십진수를 2로 나눈 몫이 2보다 작아질 때까지 계속 나눔
# 몫이 0이되는 순간 중단
# 중간 나눗셈 과정에서 발생한 나머지를 기록하고,
# 몫이 2보다 작아졌으면 거꾸로 기록하면 완성

# 나머지를 기록할 리스트
arr=[]

while decimal !=0:
    arr.append(decimal%2)
    # 2로 나눈 몫을 다음에 다시 2로 나눌것
    decimal = decimal //2

arr.reverse()

print(*arr)

# 다시 십진수로 바꿔보자
N= len(arr)
dec = 0
for i in range(N):
    dec += (2**i) * arr[N-1-i]

print(dec)
