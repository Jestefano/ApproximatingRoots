# -*- coding: utf-8 -*-
"""
Tested functions
"""
from polynomial import *
from fractionFinal import *

def iteration(y,num=5):
    """ Aguanta hasta 10 iteraciones"""
    pol = polynomial([fraction(0),fraction(1)])
    for i in range(num):
        pol =pol.recursion(y)
    leadTerm = pol.coef[-1]
    #pol.reduce()
    return pol,leadTerm

def extractionLostRoot(start,iterated):
    productNotLostRoots = iterated.coef[0]*iterated.coef[-1]
    productAllRoots = start.coef[0]
    return productAllRoots/productNotLostRoots