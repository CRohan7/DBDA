#Function top multiple all odd nos from 1 to 100

def add_mul():
    mul=1
    for i in range (1,101,2):
        
        mul=mul*i
        
    print(mul)

add_mul()