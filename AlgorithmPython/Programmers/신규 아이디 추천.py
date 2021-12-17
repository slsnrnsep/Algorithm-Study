import re


def solution(new_id):
    # 1단계 대문자를 소문자로 다 만들기
    print("1단계 : ", new_id.lower())
    new_id2 = new_id.lower()
    # 2단계 소문자,숫자,빼기,밑줄,마침표 제외한 모든 문자 제거
    for i in new_id2:
        if i.islower() or i.isdigit() or i in ["-", "_", "."]:
            answer += i
    # print("2단계 : ",re.findall("\w",new_id2))
    # 3단계 마침표가 2번이상 연속된다면 하나로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
        print(answer)
    # 4단계 .가 처음이나 끝에 위치한다면 삭제
    if answer[0] == '.':
        if (len(answer) >= 2):
            answer = answer[1:]
        else:
            answer = "."
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5단계 - 빈 문자열일 경우 a를 대입
    if answer == "":
        answer = "a"
    # 6단계 - 16자리 이상인경우 15개까지만 [0,14]까지 출력
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7단계 - 2자 이하인 경우 마지막문자를 3의 길이가 될때까지 반복해서 붙임
    if len(answer) <= 3:
        answer += answer[-1]

    return answer