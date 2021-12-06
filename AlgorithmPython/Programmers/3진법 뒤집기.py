# 자연수 n이 매개변수로 주어집니다.
# n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를
# return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.



#3진법으로 교체
#뒤집기(reverse)
#10진법으로 변환



def solution(n):
    # three =int(n,3)
    # reverse_three = "".join(reversed(three))
    #
    # ten = int(reverse_three,10)
    # return ten









def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력