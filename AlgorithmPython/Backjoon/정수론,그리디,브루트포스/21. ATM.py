N = int(input())
Time = list(map(int,input().split()))
Time.sort() #1
Total_Time = 0
Wait_Time = 0



for i in Time:  #2
    Wait_Time += i  #3
    Total_Time += Wait_Time #4
print(Total_Time)