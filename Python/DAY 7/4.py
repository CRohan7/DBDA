#Function with no retun defined by default returns 'None'

def add_mul():
    mul=1
    for i in range (1,101,2):
        
        mul=mul*i
        
    print(mul)

f=add_mul() 

print(f)