"""
2. take a list 'l1' of even nos between 150 to 250. Print its length.
Then create another list 'l2' using 'l1', 
containing only nos divisible by 4 from 'l1'.
"""

l1=[]
for i in range (150,250,2):
    l1.append(i)


print(l1)

l2=[element for element in l1 if element%4==0]
print(l2)