# 2. Write a Python function to sum all the numbers in a list. 
def check(li:list):
    
    #print(sum(li)) or

    sum=0
    for i in li:
        sum=sum+i
    print(sum)


l=[8, 2, 3, 0, 7]
check(l)