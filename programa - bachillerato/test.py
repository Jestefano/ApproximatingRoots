import os
os.chdir('C:\\Users\\LENOVO\\Desktop\\tesis\\programa')
#%%
from fractionFinal import *
from polynomial import *
from AuxiliarFunctions import *
#%%
def factor(poly,iterations,eps):
    if(poly.degree()==1):
        return [fraction(-1)*poly.coef[0]/poly.coef[1]]
    if(poly.degree()==0):
        return []
    aux = iteration(poly,iterations)[0]
    spCase = 0
    
    if(aux.coef[0]==fraction(0)):
        spCase=1
    else:
        root = extractionLostRoot(poly,aux)
        if(abs(poly.evaluate(root))>eps):
            root = fraction(-1)*root
        #Is it root?
        if(abs(poly.evaluate(root))>eps):
            spCase=1
        
    if(spCase):
        #Complex root or inside M
        prevIteration = iteration(poly,iterations-1)
        
        ## Verificar el termino de mayor grado
        if(prevIteration[1].decimal()<1000):###!!
            #And all roots are inside M
            print('### Traslacion')
            return [factor(poly.move(fraction(3)),iterations,eps)]
        else:
            #Complex root
            difIterations = aux - prevIteration[0]
            difIterations.reduce()
            division = poly.divisionPolynomial(difIterations)
            return factor(difIterations,iterations,eps)+[division[0]]
    else:
        newPoly = poly.divisionPolynomial(polynomial([fraction(-1)*root,fraction(1)]))
        roots = factor(newPoly[0],iterations,eps)
        return roots + [root]

#%%
def factorization(poly,iterations=8,eps=0.01):
    roots = []
    while(poly.degree()>1 and abs(poly.evaluate(fraction(0)))<0.0001):
        poly.coef = poly.coef[1:]
        roots.append(fraction(0))
    #we get a polynomial without 0 as root
    return roots + factor(poly,iterations,eps)
#%%

def printRoots(l):
    for i in l:
        if(str(type(i))=="<class 'list'>"):
            print('?')
            for j in i:
                print(j+fraction(4))
            print('?')
        else:
            print(i)


y = polynomial([fraction(-1,2),fraction(1,2),fraction(1,2),fraction(1)])
y = y.move(fraction(3))
y.reduce()
print(y)

#print(factor(y,7,0.1)[0])

for i in range(1,7):
    print(iteration(y,i)[0])
