# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:50:46 2018

@author: peich
"""
#new comment
import random as rd
from collections import Counter

"""La siguiente función no da valores por sí misma, sino que hay que invocarlos
con el método __next__() en Python2. Define 'a=ngen(n)' y luego a.__next__() 
las veces que desees"""

def ngen(n):
    num = 0
    while(num < n):
        yield num
        num += 1


def quadgen(n):
    a = 1
    while(a < n):
        yield a**2
        a += 1


def fibogen(n):
    a, b = 0, 1
    while(b < n):
        yield a + b
        a, b = b, a+b


def logistgen(n,r):
    a = .5
    while(a < n):
        yield a
        a = r*a*(1-a)


def pseudopoisson(tmax):
    t, x, i = 0, 0, 0
    while(t < tmax):
        yield x
        if rd.random() > 2**-i:
            x += 1
            i = 0
        else:    
            i += 1
        t += 1

