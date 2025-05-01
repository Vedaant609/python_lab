class weather:
    def __init__(self,w):
        self.weather = w
        
    def __contains__(self,i):
        return i in self.weather
a = weather(["a",'b','c','d','e'])
print ('a' in a)
