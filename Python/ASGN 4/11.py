"""

11. Take a number as input from user. 
Print maximum and minimum integer which can be generated using all the digits in the input number
Ex. Input 3421   : o/p max: 4321, min 1234
Input 7789    : o/p max: 9776   min 6779


"""


num=(input("Enter Number: "))
l1=[]
lmin=[]
lmax=[]
for i in num:
    l1.append(i)
    l1.sort()
m=''
for j in l1:
    k=str(j)

    m=m+k
    
print("MIN: " ,m)

lmax=l1[::-1]
m=''
for s in lmax:
    p=str(s)

    m=m+p
    
print( "MAX:", m)
