"""

3. two strings, s1, and s2 return a new 
string made of the first, middle, and last 
characters each input
string
Given:
s1 = "America"
s2 = "Japan"
Expected Output:
AJrpan

"""
s1 = "America"
s2 = "Japan"

mid1=(len(s1)//2)

mid2=(len(s2)//2)

print(s1[mid1])   
print(s2[mid2]) 

s3=s1[:1]+s2[:1]+s1[mid1]+s2[mid2]+s1[-1:]+s2[-1:]
print(s3)
