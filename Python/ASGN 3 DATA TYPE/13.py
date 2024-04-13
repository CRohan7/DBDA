"""
#A
print(int.bit_length(10))

print(bin(10))

#B
import math
num=float(input("Enter Number: "))
sq=math.sqrt(num)
if(isinstance(sq,float)):
    print("Perfect Square Number")


c. Take hexadecimal string from user and 
convert it to float
Ex. User input string: '0x1.67e30'
o/p 1.4058074951171875
"""
num=hex(input("Enter Hexa String: "))
print(float(num,16) )

