class employee:
    def __init__( self, empid , name, desig , salary ,pro_id , skills):
        self.empid=empid
        self.name=name
        self.desig=desig
        self.__salary = salary
        self.pro_id=pro_id
        self.skills=skills
        

        employee.company_name = "USIT"

    def info(self):
        print("EMPID:", self.empid ,"\nEMPNAME:", self.name ,"\nDESIGNATION:" ,self.desig ,"\nCOMPANY:" ,employee.company_name )


    def check(self):
        
        for i in self.skills:
            if( i=="Python"):
                print( "\nFROM SKILLS"  ,  "\nID: ", self.pro_id , "\nNames: ", self.name , "\nSkills:" , self.skills)

    @classmethod
    def comp_details(cls):
        print("\nCompany name:" , cls.company_name)

    @staticmethod    
    def st():
        print("Company name:" , employee.company_name)
        print("ENAME:" , employee.ename)







##########################################################################
pro1={1,2,3}
pro2={1,2,5}
pro3={2,5,7}
s1=[ "Python" ,"JAVA" , "C" ]
s2=[ "Python" , "JAVA" , "C++" ]
s3=["JAVA", 'C++']


###################################################################################
for i in range(1,4):
    print("ENTER DETAILS FOR EMPLOYEE NO",i)
    idd=int(input("Enter Id:"))
    name=(input("Enter Name:"))
    position=(input("Enter Designation: "))
    sal=int(input("Enter Sal: "))
    if(i==1):
        e1=employee(idd,name,position,sal,pro1,s1)
    elif(i==2):
        e2=employee(idd,name,position,sal,pro2,s2)
    elif( i==3 ):
        e3=employee(idd,name,position,sal,pro3,s3)

##########################################################################3

print()
print("EMP1 Identity")
e1.info()

print()
print("EMP2")
e2.info()

print()
print("EMP3")
e3.info()
#################################################################################

e1.check()
e2.check()
e3.check()

#################################################################################
e1.comp_details()
e2.comp_details()
e3.comp_details()