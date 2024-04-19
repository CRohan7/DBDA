class A:
    def __init__(self):
        self.a=100
        print(self.a)

class B:
    def __init__(self):
        self.b=15
        print(self.b)

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c=self.a+self.b
        print(self.c)

C()
        