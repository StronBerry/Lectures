class Parent:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Child(Parent):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c