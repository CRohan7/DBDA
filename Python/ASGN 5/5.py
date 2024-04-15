"""
5. create a third-string made of the
 first char of s1 then the last char of s2,
 Next, the second char of s1
and second last char of s2, and so on. 
Any leftover chars go at the end of the result.
Given:
s1 = "Abc"
s2 = "Xyz"
Expected Output:
AzbycX

"""
s1 = "Abc"
s2 = "Xyz"

s=0
e1=len(s1)-1

e2=len(s2)-1

s3=s1[0]+s2[e2]+s1[1]+s2[e2-1]+s1[2]+s2[e2-2]

print(s3)




