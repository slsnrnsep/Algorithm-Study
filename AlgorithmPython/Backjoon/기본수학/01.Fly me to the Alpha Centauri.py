
# 5
def count(distance):
    i=0
    while i<=distance:
        if(distance>i*i and distance<=i*i+i):
            return 2*i

        elif(distance<=(i+1)*(i+1)):
            return i*2+1
        i= i+1


T = int(input())

for z in range(T):
    a,b = map(int,input().split())
    print(count(b-a))