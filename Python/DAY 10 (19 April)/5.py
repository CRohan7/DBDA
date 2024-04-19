# SIMPLE
class A:
    def __init__(self):
        self.a=100

class B(A):
    def __init__(self):
        self.b=150
        super().__init__()
obj=B()
print(obj.b)
print(obj.a)