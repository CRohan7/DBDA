"""

9.	Write a program to check whether an years is leap year or not the year is leap if
 it satisfies following condition  
 It the year is divisible by 100 o If it is divisible by 100, then
 it should also be divisible by 400 then it is leap year 
 otherwise, all other years divisible by 4 and not divisible by 100 then it is leap year.  

"""
while(1):
    year=int(input("Enter Year: "))

    if(year%400==0):
        print("Leap Year!")
    elif((year%100==0) & (year%400==0) ):
        print("Leap Year!")
    elif(year%4==0):
        print("Leap Year!")
    else:
        print("Not a leap year")


    print(year)