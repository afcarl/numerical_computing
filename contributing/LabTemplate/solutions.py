import math

def euclidean(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

class ComplexNumber(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    def __str__(self):
        return "{} + {}i".format(self.real, self.imag)
    
    def __repr__(self):
        return str(self)
    
def custom_complex(x, y):
    n = ComplexNumber(x, y)
    return n, n.norm()

        