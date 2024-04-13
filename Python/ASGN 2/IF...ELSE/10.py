"""

10. Write a program to accept the price of a bike and 
display the road tax and insurance to be paid according to the following criteria . 
also display total amount to be paid.  
      
        Cost price (in Rs)           Tax                Inssurance  
        > 100000                     15 %                   20%  
        > 50000 and <= 100000        10%                    8%  
        <= 50000                     5%                     5%   

"""

price=float(input("Enter Price"))

tax=0.00
insurance=0.0
total=0.0
if(price>100000):
    tax=0.15*price
    insurance=0.2*price
elif( 50000>price<=1000000 ):
    tax=0.1*price
    insurance=0.08*price
elif(price<=500000):
    tax=0.05*price
    insurance=0.05*price
total=tax+insurance
print(tax)
print(insurance)
print(total)
