## Clase fraccion:
class fraction():
    def __init__(self,numerator,denominator=1):
        assert str(type(numerator))=="<class 'int'>", 'Numerator is not integer'
        assert str(type(denominator))=="<class 'int'>", 'Denominator is not integer'
        assert denominator!=0, 'Denominator is zero'
        self.numerator = numerator
        self.denominator = denominator
        
    def fractionSimplification(self):
        """
        Fraction simplification only for numbers that are small enough! 
        Not members of a big iteration
        """
        aux = "{0:.10f}".format(self.decimal()).split('.')
        s = int(aux[0]+aux[1])
        return fraction(s,10**len(aux[1])).reduce()
        
    def reduce(self):
        from math import gcd
        aux = gcd(self.numerator,self.denominator)
        return fraction(self.numerator//aux,self.denominator//aux)

    def __add__(self,other):
        assert(str(type(other)))[-11:]==".fraction'>", 'Other is not a fraction'
        aux = fraction(self.numerator*other.denominator+other.numerator*self.denominator,
        self.denominator*other.denominator)
        aux = aux.reduce()
        return aux
    
    def __mul__(self, other):
        assert(str(type(other)))[-11:]==".fraction'>", 'Other is not a fraction'
        aux = fraction(self.numerator*other.numerator,self.denominator*other.denominator)
        return aux.reduce()
    def __sub__(self,other):
        return fraction.__add__(self,fraction(-1)*other)
    def __truediv__(self, other):
        assert(other.numerator!=0), "Denominator is zero"
        aux = self*fraction(other.denominator,other.numerator)
        aux = aux.reduce()
        return aux
    def decimal(self):
        return self.numerator/self.denominator
    def __str__(self):
        return str(self.decimal())
    def __ge__(self, other): 
        return self.numerator*other.denominator >= self.denominator*other.numerator
    