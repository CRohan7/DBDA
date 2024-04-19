#MULTILEVEL
class A:
    def __init__(self) :
        self.a=100
        print(self.a)


class B(A):
    
    def __init__(self) :
        super().__init__()
        self.b=self.a+50
        print(self.b)

class C(B):
    def __init__(self):
        super().__init__()
        self.c=self.b+50
        print(self.c)
    
C()