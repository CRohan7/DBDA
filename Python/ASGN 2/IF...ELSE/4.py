"""
4.	A school has following rules for grading system:  
a.	Below 25 - F  
b.	25 to 45 - E  
c.	45 to 50 - D  
d.	50 to 60 - C  
e.	60 to 80 - B  
f.	Above 80 - A  
Ask user to enter marks and print the corresponding grad

"""

while(1):
    marks=int(input("Enter Marks: "))
    grade='o'
    if(marks>80):
        grade='A'
    elif(60<marks<=80):
        grade='B'
    elif(50<marks<=60):
        grade='C'    
    elif(45<marks<=50):
        grade='D'
    elif(25<marks<=45):
        grade='E'
    elif(0<marks<25):
        grade='F'
    print(grade)