#피보나치 수열의 n번 항 구하기
def fibo(n):
    if n < 2:
        #0번항, 1번항 => 0,1
        return n
    else:
        # 나머지 : n-1번항 + n-2번항
        return fibo(n-1) + fibo(n-2)

print(fibo(7))
