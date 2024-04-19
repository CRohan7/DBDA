#Data Hiding

class info:
    def __init__(self):
        self.name=200
        self.__hidden="From the hidden"

ht=info()
print(ht.__hidden)
print(ht.info__hidden)
