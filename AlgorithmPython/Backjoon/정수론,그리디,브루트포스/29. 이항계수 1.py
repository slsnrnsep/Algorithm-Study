from math import factorial as fac
import sys
input=sys.stdin.readline

N, K = map(int, input().split()) # 자연수 N과 정수 K 입력

# 팩토리얼 함수
def fact(N) :
    if N<=1 :
        return 1

    return N * fact(N-1)

# nCr 구하는 공식 사용
print(fact(N) // (fact(K) * fact(N-K)))