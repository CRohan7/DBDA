"""


10. Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
output:
[5, 15, 25, 50]


"""

list1 = [5, 10, 15, 20, 25, 50, 20]
for i in list1:
    if(i==20):
        a=list1.index(20)
        list1.pop(a)
        

print(list1)