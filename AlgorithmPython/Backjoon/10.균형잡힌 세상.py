while(1):
    s = input().rstrip()
    if s == '.':
        break

    box = []
    flag = True

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            box.append(s[i])

        elif box and (s[i] == ')' or s[i] == ']'):  #
            if s[i] == ')' and box[-1] == '(':
                box.pop()
            elif s[i] == ']' and box[-1] == '[':
                box.pop()
            else:  # (])
                flag = False

        elif not box and (s[i] == ')' or s[i] == ']'):  # stack이 없으면서 닫힌 괄호가 나오는 경우, )(
            flag = False

    if flag and not box:
        print('yes')
    else:
        print('no')