"""
7.Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :  
             Unit                                    Price    
First 100 units                                       no charge  
Next 100 units                                        Rs 5 per unit  
After 200 units                                       Rs 10 per unit  
(For example if input unit is 350 than total bill amount is Rs2000)  
"""

unit=int(input("Enter Units: "))
charge1=0
charg2=0
if(unit>200):
    rem=unit-200
    charge1=rem*10
    charge2=100*5
final=charge1+charge2
print('Charge is',' $',final,sep='')

