'''
Created on Jul 20, 2013

@author: noah
'''

import main as m


def sum_(args):
    if isinstance(args[0], list):
        ls = []
        l = args[0]
        for i in args: ls.append(l[i])
        return sum(ls)