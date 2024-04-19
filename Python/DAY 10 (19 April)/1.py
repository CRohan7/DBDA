"""
write a program to creatr class course having variables 
course_id , course_name , duration , total_hours , contents , staff_count , agency

and methods : display_info , display_agency



"""


class course :
    def __init__(self, course_name,course_id , duration , total_hours , contents , staff_count , agency) :
        self.course_name=course_name
        self.course_id=course_id
        self.duration=duration
        self.total_hours=total_hours
        self.contents=contents
        self.staff_count=staff_count
        self.agency=agency

    def display_info(self):
        print( self.course_name)
        print(self.course_id)
        print(self.duration)

    def display_agency(self):
        print(self.agency)

    @classmethod
    def dis_agency(cls):
        print(cls.agency)


rohan=course('DBDA' , 15 ,'6 months' ,500 , 'Big data' , 10 , 'DTE')
rohan.display_info()
rohan.display_agency()



        


        