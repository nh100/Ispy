'''
Created on Jul 20, 2013

@author: noah
'''

import main as m


def sum_(args):
    if isinstance(args[0], list):
        return sum(m.eval_(args[0]))
    
def fst(args):
    if not isinstance(args[0], list):
        m.panic("argument not list")
    else: return m.eval_(m.eval_(args[0])[0])

def tail(args):
    return m.eval_(m.eval_(args[0])[1:])