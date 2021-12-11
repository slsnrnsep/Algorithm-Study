board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                stack.append(board[j][i-1])
                board[j][i-1] = 0 # 없어도 됨
                break
        if(stack[-1] == stack[-2]):
            stack.pop()
            stack.pop()
            answer += 1

    return 2 * answer


solution(board,moves)


