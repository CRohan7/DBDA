# SIMPLE using explicit parent class initialiation

class A:
    def __init__(self):
        self.a=100
class B(A):
   
    def __init__(self):
        A.__init__(self)
        self.b=self.a+10
        print(self.b)

B()
