#1. Write a Python function to find the maximum of three numbers. 

def check(x,y,z):
    l=[]
    l.append(x)
    l.append(y)
    l.append(z)
    print("Max: ", max(l))

a,b,c=1,4,3

check(a,b,c)