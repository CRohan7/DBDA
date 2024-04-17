# 16. Write a Python function to create and
# print a list where the values are the 
# squares of numbers between 1 and 30 
# (both included). 

def check():
    l=[]
    for i in range(1,31):
        l.append(i*i)
    print(l)
check()
