"""

8.	Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.  


"""

num=(input("Enter Number: " ))
l1=[]
for i in num:
    l1.append(i)
l2=l1[::-1]
i=int(l2[0])

print(i)
if(i%3==0):
    print("Divisible by 3")
else:
    print("Not divisible")