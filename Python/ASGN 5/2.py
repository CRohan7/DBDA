"""


2. Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
Given:
s1 = "Ault"
s2 = "Kelly"
Expected Output:
AuKellylt



s1 = "Ault"
s2 = "Kelly"

mid1=(len(s1)//2)-1
s3=s1[:mid1+1]+s2+s1[mid1+1:]

print(s3)
"""


s1=input("Enter String 1:")
s2 = "xxxx"


ls1=len(s1)
mid1=0
if(ls1%2==0):
    mid1=(len(s1)//2)-1
else:
    mid1=(len(s1)//2)


s3=s1[:mid1+1]+s2+s1[mid1+1:]

print(s3)



