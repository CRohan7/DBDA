"""
2. accept amount from user and find the minimum number notes required to get the amount amount =512  
Notes: 2000,500,100,50,10,5,2,1  

500-1 note  
10  - 1 note  
2-  1 coin  

amount=20550  
2000 – 10 note  
500 – 1 note  
50 -1 note 

"""


total=int(input("Enter Number: "))
#2000
notes_2k=total//2000
rem_2k=total%2000
print('2000: ', notes_2k)

#500
notes_500=rem_2k//500
rem_500=rem_2k%500
print('500: ',notes_500)

#100
notes_100=rem_500//100
rem_100=rem_500%100
print('100: ', notes_100)


#50
notes_50=rem_100//50
rem_50=rem_100%50
print('50: ', notes_50)


#10
notes_10=rem_50//10
rem_10=rem_50%10
print( '10: ', notes_10)

#5
notes_5=rem_10//5
rem_5=rem_10%5
print('5: ', notes_5)

#2
notes_2=rem_5//2
rem_2=rem_5%2
print( '2: ',notes_2)

#1
notes_1=rem_2//1

print('1: ',notes_1)
