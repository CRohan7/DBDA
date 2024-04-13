"""
6.	Accept number from user and 
check whether it is divisible by 5 and 11 if divisible then display appropriate message. 

"""

num=int(input("Enter Number: "))

if((num%5==0) & (num%11==0)):
    print("Divisble by 5 and 11")
else:
    print("Not Divisible")
        