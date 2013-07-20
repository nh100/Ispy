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