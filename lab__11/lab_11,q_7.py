class string:
    def __init__(self,c):
        self.c = c
    def __iadd__(self,other):
        self.c += other
        return self.c
    def toLower(self):
        return self.c.lower()
    def toUpper(self):
        return self.c.upper()
a = string("fkjhdlfgkjfgjhfd")
b = "were"

print(a.toUpper())
