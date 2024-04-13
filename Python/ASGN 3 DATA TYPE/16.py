"""
Q16. WAP to check given integer is a perfect square or not. 
Don't use built in function
"""
while(1):
    num=float(input("Enter Number: "))
    sq=num**0.5
    q=int(sq)
    p=sq%q
    if(p==0):
        print("Perfect Square of ",q)
    else:
        print("Not Perfect")