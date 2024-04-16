# 7. Write a Python function that 
# accepts a string and counts the 
# number of upper and lower case 
# letters. 
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12
def check(st:str):
    lcount=0
    ucount=0
    for i in st:
        if(i.islower()):
            lcount+=1
        elif(i.isupper()):
            ucount+=1
    print("Lower: ", lcount)
    print("Upper: ", ucount)
    
s=input("Enter String: ")
check(s)

