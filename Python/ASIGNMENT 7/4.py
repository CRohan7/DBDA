# Q WA function to check if number is prime or not. 
# Return True if number is prime and false if number not prime.
import math
def check(num:int):
    sqr= math.ceil(num**0.5)
    count=0
    for i in range(2,sqr):
        if((num%i)==0):
            count+=1
    if count>0:
        return False
    else:
        return True

num=int(input("Enter num: "))
c=check(num)

print(c)