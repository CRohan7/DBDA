"""

12. Take integer from user and print all odd numbers which can be generated using any number of digits from given number
Ex. 
Input: 3421  o/p: 1,3,13,43,23,31,41,21,421,241,341,431,423,243,143,413,1243,1423,4213,4123, 2413,2143, .. etc


"""


num=(input("Enter Integer: "))

list1=[  ]
for j in num:
    #j=int(i)
    list1.append(j)

list2=[]

print(list1)
for a in list1:
    for z in list1:
        for i in list1:
            for j in list1:

                if((a==z)  & (a==i) & (a==j)):
                    continue
                if((z==a)  & (z==i) & (z==j)):
                    continue
                if((i==a)  & (i==z) & (i==j)):
                    continue
                if((j==a)  & (j==z) & (j==i)):
                    continue
                c=i+j+z+a
                p=int(c)
                if(p%2!=0):
                    list2.append(p)
print(list2)
                    
# cant eliminate duplicate digits