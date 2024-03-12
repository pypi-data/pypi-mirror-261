class qMath:
    from . import TsallisMath as Ts
    q = 1.0
    type = 1.0

    def __init__(self, q, type):
        self.q = q
        self.type = type

    def __str__(self):
        return f'q = {self.q}, type is {self.type}'

    def qexp(self,value):
        return self.Ts.qexp(value, self.q, self.type)
    
    def qlog(self,value=1.0):
        return self.Ts.qlog(value,self.q,self.type)
    
    def qX(self,q = 1.0,value=0.0, type = 1):#type could be 1,2,3
       return self.Ts.qX(value,self.q,self.type)