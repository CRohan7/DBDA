"""
4. Print two lists in the following order
list1 = [5, 6,7]
list2 = [0, 1]
output:
50,51,60,61,70,71

"""
l1 = [5, 6,7]
l2 = [0, 1]

for i in l1:
    for j in l2:
        a=str(i)+str(j)
        print(a,end=' ')
