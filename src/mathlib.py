'''
Created on Jul 18, 2013

@author: noah
'''

import math
import main as m

        
def pi(args):
    return math.pi
                                                
def sqrt_(args):
    return math.sqrt(m.eval_(args[0]))
                                                
def sq(args):
    return m.eval_(args[0])**2  

def abs_(args):
    return abs(m.eval_(args[0]))          

def even(args):
    return m.eval_(args[0]) % 2 == 0

def odd(args):
    return m.eval_(args[0]) % 2 != 0       

def is_prime(args):
    for i in range(2, m.eval_(args[0])):
        if m.eval_(args[0]) % i == 0: return False
    return True

