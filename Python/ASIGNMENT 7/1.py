#Q WA function to take a number as parameter and 
#  print True if given number is even else print False


def check(num):
    if((num%2)==0):
        print("True")
    else:
        print('False')

num=int(input("Enter Number: "))
check(num)
