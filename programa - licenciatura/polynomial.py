from fractionFinal import *

class polynomial():
    def __init__(self,coef=[]):
        self.coef = coef
        
    def __mul__(self,other):
        assert(str(type(other))[-13:]==".polynomial'>"),'Not a polynomial'
        deg_self = len(self.coef)-1
        deg_other = len(other.coef)-1
        new_coef = [fraction(0) for i in range(deg_self+deg_other+1)]
        for x,i in enumerate(self.coef):
            for y,j in enumerate(other.coef):
                new_coef[x+y]+=i*j
        new_ = [fraction(0) for i in range(deg_self+deg_other+1)]
        for j,i in enumerate(new_coef):
            new_[j] = i.reduce()
        return polynomial(new_)

    def __add__(self,other):
        assert(str(type(other))[-13:]==".polynomial'>"),'Not a polynomial'
        coef_aux = [fraction(0) for i in range(max(len(self.coef),len(other.coef)))]
        for pos,i in enumerate(self.coef):
            coef_aux[pos] += i
        for pos,i in enumerate(other.coef):
            coef_aux[pos] += i
        coef = [fraction(0) for i in range(max(len(self.coef),len(other.coef)))]
        for pos,i in enumerate(coef_aux):
            coef[pos] = i.reduce()
        return polynomial(coef_aux)

    def __sub__(self,other):
        aux =  self + polynomial([fraction(-1)])*other
        while(len(aux.coef)>0 and abs(aux.coef[-1].decimal())<0.0001):
            aux.coef = aux.coef[:-1]
        if(len(aux.coef)==0):
            aux.coef = [fraction(0)]
        return aux
    
    def simplification(self,poly):
        if(len(self.coef)>=len(poly.coef)):
            #polynomio que queda:
            c = self.coef[-1]
            self.coef = self.coef[:-1]
            pol_red = [fraction(0)]*(len(self.coef)+2-len(poly.coef))
            pol_red[-1] = c
            pol_red = polynomial(pol_red)
            #polinomio reemplazo:
            poly_aux = polynomial([fraction(-1)*x for x in poly.coef[:-1]])
            poly_aux = poly_aux*pol_red
            self = polynomial.simplification(self+poly_aux,poly)
        return self
    
    def recursion(self,poly):
        return polynomial.simplification(self*self+polynomial([fraction(0),fraction(1)]),poly)
    
    def __str__(self):
        temporal = []
        for i in self.coef:
            temporal.append(i.__str__())
        return str(temporal)
    def degree(self):
        return len(self.coef)-1
    
    def divisionPolynomial(self,other):
        """This function divides self by other, and returns a polynomial"""
        if(self.degree()<other.degree() or (self.degree()==0 and abs(self.coef[0].decimal())<0.0001)):
            return polynomial([fraction(0)]), self
        auxiliarCoef = (self.coef[-1] / other.coef[-1])
        auxiliarPoly = [fraction(0)]*(self.degree()-other.degree()+1)
        auxiliarPoly[-1] = auxiliarCoef
        auxiliarPoly = polynomial(auxiliarPoly)
        rec = polynomial.divisionPolynomial(self-other*auxiliarPoly,other)
        return rec[0] + auxiliarPoly,rec[1]
    
    def evaluate(self,number):
        val = 0
        for i,j in enumerate(self.coef):
            val += j.decimal()*number.decimal()**i
        return val
    def reduce(self):
        num = self.coef[-1]
        while (abs(self.coef[-1].decimal())<0.00001 and len(self.coef)>1):
            self.coef = self.coef[:-1]
        if(abs(self.coef[-1].decimal())<0.00001 and len(self.coef)==1):
            return None
        newCoef = self.coef.copy()
        for i,j in enumerate(self.coef):
            newCoef[i] = (j/num).fractionSimplification()
        self.coef = newCoef
    def closeToZero(self,eps):
        for i in self.coef:
            if(abs(i.decimal())>eps):
                return False
        return True
    
    def move(self,num):
        """This function moves all the roots num"""
        polyResult = polynomial([self.coef[0]])
        for j,i in enumerate(self.coef[1:]):
            aux = polynomial([num,fraction(1)])
            res = polynomial([i])
            for k in range(j+1):
                res = res*aux
            polyResult = polyResult + res
        return polyResult
        
        