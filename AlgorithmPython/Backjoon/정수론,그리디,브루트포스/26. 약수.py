import sys

input = sys.stdin.readline
t = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

n = arr[0] * arr[-1]
print(n)
