"""
I’m happy to share that I’ve started my Diploma of Education at Centre for Development 
of Advanced Computing (C-DAC) IN DBDA !

6. Remove empty strings from the list of strings
list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
output:
["Ashish", "Atharva", "Amit", "Revati"]


"""

list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]


#1 
#l2=[ e for e in list1 if e>"" ]
#print(l2)


#2 not working

list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]


for i in list1:
        u=bool(i)
        print(u)
        if(u==False):
                list1.remove(i)
    

print(list1)


