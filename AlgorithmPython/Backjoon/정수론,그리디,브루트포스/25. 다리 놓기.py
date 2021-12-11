# 1. 테스트 케이스 수 : t
t = int(input())

for i in range(t):
    # 2. 서쪽 사이트 개수, 동쪽 사이트 개수 : n,m
    n, m = map(int, input().split())

    # 3. 다리를 지을 수 있는 개수
    if n == 0:
        print(0)
        continue

    count = 1

    for j in range(n):
        count = count * (m - j)

    for j in range(1, n + 1):
        count = count // j

    print(count)

    # from math import factorial as fac
    #
    # W = []
    # E = []
    # C = []
    #
    # while (1):
    #     try:
    #         t = int(input())
    #         break
    #     except:
    #         continue
    #
    # for i in range(t):
    #     west, east = input().split()
    #     W.append(west)
    #     E.append(east)
    #
    #     if W[i] > E[i]:
    #         C.append(0)
    #     elif W[i] == E[i]:
    #         C.append(1)
    #     else:
    #         C.append(fac(E[i]) // fac(E[i] - W[i]) // fac(W[i]))
    #
    # for j in range(t):
    #     print(C[j])
