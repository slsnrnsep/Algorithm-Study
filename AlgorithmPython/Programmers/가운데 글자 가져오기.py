# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
#
# 재한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.


def solution(s):
    answer = ''
    c=int(len(s)/2)
    if(len(s)%2==0):
        answer = s[c-1] + s[c]
    else:
        answer = s[c]
    return answer


solution("abcde")