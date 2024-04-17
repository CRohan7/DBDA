# 5. Write a Python function to 
# calculate the factorial of a number
#  (a non-negative integer). The 
# function accepts the number as 
# an argument. 


def check(n:int):
    fac=1
    for i in range(2,n+1):
        fac=fac*i
    print(fac)
check(7)
