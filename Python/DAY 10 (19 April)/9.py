# method overridding


class A:
    def __init__(self):
         pass
    
    def info(self):
            print("From A")

#class B:


class C(A):
    def __init__(self):
        super().__init__()
    
    def info(self):
        print("From C")
obj=C()
obj.info()