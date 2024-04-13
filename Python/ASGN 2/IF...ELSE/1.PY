"""
1.	A student will not be allowed to sit in exam if his/her attendence is less than 75%.  
Take following input from user Number of classes held Number of classes attended. And print percentage of class attended  
Is student is allowed to sit in exam or not.  

"""

total=int(input("Enter Total: "))
attended=int(input("Enter Attended: "))

per=(attended/total)*100
if(per>75):
    print("Allowed!")
else:
    print("Not Allowed!")