def solution(answers):
    sufo1 = [1, 2, 3, 4, 5]
    sufo2 = [2, 1, 2, 3, 2, 4]
    sufo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    scores = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == sufo1[i % len(sufo1)]:
            scores[0] += 1
        if answers[i] == sufo2[i % len(sufo2)]:
            scores[1] += 1
        if answers[i] == sufo3[i % len(sufo3)]:
            scores[2] += 1

#가장 높은 점수를 받은사람이 다수일경우 , 오름차순 정렬 리턴
    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score:
            #결과값의 인덱스에는 몇번 학생인지가 와야하니
            answer.append(i + 1)
    return answer


solution([1,3,2,4,2])