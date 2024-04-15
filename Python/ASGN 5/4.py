"""

4. Given an input string with the 
combination of the lower and upper case
arrange characters in such a
way that all lowercase letters should 
come first.

a=97
z=122
A=65
Z=90
"""
name="Rohan"
l1=[]
for i in name:
    l1.append(i)

print(l1)

l2=[]
for i in l1:
    asci=ord(i)
    l2.append(int(asci))
print(l2)

for i in l2:
    print(i)
    if(64<i<91):
        #captial
        print(chr(i))

    elif(96<i<122):
        #for small
        print(chr(i))



"""
st=input("Enter String: ")
low=[]
up=[]
for i in st:
    if (i.islower()):
        low.append(i)
    else:
        up.append(i)
print(low)
print(up)

final="".join(low+up)
print(final)
   

"""
