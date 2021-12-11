# T = int(input())
#
#
# def test(string):
#     a= string.count('(')
#     b= string.count(')')
#
#     if a==b:
#         return "YES"
#     else:
#         return "NO"


# for _ in range(T):
#     input_string = input()
#     print(test(input_string))

num = int(input())

for i in range(num):
  input_data = input()
  box = []

  for j in input_data:
    if j == '(':
      box.append(j)
    elif j == ')':
      if len(box) != 0 and box[-1] == "(":
        box.pop()
      else:
        box.append(")")
        break

  if len(box) == 0:
    print("YES")
  else:
    print("NO")
