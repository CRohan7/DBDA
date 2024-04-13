"""
3.	Modify the above question Q1 to allow student to sit if he/she has medical cause. 
Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.  

"""

total=int(input("Enter Total: "))
attended=int(input("Enter Attended: "))
cause=input("Medical Cause? (Y/N): ")

per=(attended/total)*100
if(cause=='Y'):
    print("Allowed!")
else:
    if(per>75):
        print("Allowed!")
    else:
        
        print("Not Allowed!")