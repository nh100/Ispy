'''
Created on Jul 21, 2013

@author: noah
'''
from sexpdata import dumps, loads, Symbol
import main
class Function(object):
    '''
    classdocs
    '''

    # private member
    def _replacel(self, l1, old, new):
        for i, n in enumerate(l1):
            if n == old: l1[i] = new
        return l1
    
    def call(self, call_args):
        # ls = [(arg, call_arg) for arg in self.args for call_arg in call_args]
        call_val = [v for v in self.val]
        for i, v in enumerate(self.args):
            call_val = self._replacel(call_val, v, call_args[i])
        return main.eval_(call_val)

    def __init__(self, args, val):
        self.args = args
        self.val = val