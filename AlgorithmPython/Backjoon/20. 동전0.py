N, K = map(int, input().split())
coins=[]
for i in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

result=0
for i in coins:
    if K==0:
      break
    result += K//i
    K = K % i

# for i in coins:
#     if i > K:
#         continue
#     else:
#         while i <= K:
#             K -= i
#             result += 1

print(result)