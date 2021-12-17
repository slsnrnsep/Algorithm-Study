def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi_tower(n - 1, start, 6 - start - end)
    print("hanoi_tower("+str(n-1) +","+str(start)+","+str(6 - start - end)+")")
    print(start, end)  # 2단계
    hanoi_tower(n - 1, 6 - start - end, end)  # 3단계
    print("hanoi_tower("+str(n-1) +","+str(6 - start - end)+","+str(end)+")")
# (3,1,3)
#
#
# (2,1,2) -> (1,1,3) -> 1,3 출력
# print(1,3) 출력
# (1,1,2) -> 출력

# def hanoi(n,a,b)
#     if n > 1:
#         hanoi(n-1, a, 6-a-b)              # 기둥이 1개 이상이면 그룹으로 묶인 n-1개 원판을
#                                           # 중간으로 먼저 다 옮긴다
#     print(a, b)
#
#     if n > 1:
#         hanoi(n-1, 6-a-b, b)



n = int(input())
print(2 ** n - 1)
hanoi_tower(n, 1, 3)