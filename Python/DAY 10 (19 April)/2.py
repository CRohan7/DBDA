

class course:
    def __init__(self,cou,idd,name,dura,hrs,cont,countt):
        self.cou=cou
        self.idd=idd
        self.idd=idd
        self.name=name
        self.dura=dura
        self.hrs=hrs
        self.cont=cont
        self.countt=countt
        course.agency='CDAC'
    
    @classmethod   #decorator
    def agen(cls):
        print( "Agency: " , cls.agency)

    def info(self):
        print("CNAME:", self.course_name)


obj=course("DBA", 6,"Rohan","^months",7,"Big",99)
obj.agen()

print(course.__dict__)
