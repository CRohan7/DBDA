# Calculate Fatorial of given number

def fact(num:int):
    product=1
    for i in range(2,num+1):
        product=product*i
    
    print(product)
    print(len(str(product)))

fact(100)

