#8. Write a Python function that
#  takes a list and returns a new list
#  with distinct elements from the 
#  first list. 
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def check(li:list):
    s=set(li)
    lnew=list(s)
    print(lnew)


l=[1,2,3,3,3,3,4,5]
check(l)