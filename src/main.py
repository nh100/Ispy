import sys
from mathlib import *
import lists as l

from sexpdata import Symbol
from func import Function
global_env = {}
VERSION = 0.2
class Panic(object):
    msg = ''
    def __init__(self, s):
        self.msg = s
    def __str__(self):
        return 'Panic: %s' % self.msg
        
def panic(s):
            sys.stderr.write(str(Panic(s)))
            print()

def panic_(args):
    panic(args[0])
         
def out(args):
    if check_args(args, 1):
        for v in args: sys.stdout.write(str(eval_(v)))
    return ''
        
def _str_add(args):
    sm = ''
    for s in args:
        sm += str(s)
    return sm

def add(args):
        sum = 0
        for i in args: 
            sum += eval_(i)
        return sum
            
def div(args):
    if check_args(args, 2):
        quot = eval_(args[0])
        for i in args[1:]:  quot /= eval_(i)
        return quot
            
def mul(args):
    if check_args(args, 2):
        prod = eval_(args[0])
        for i in args[1:]: prod *= eval_(i)
        return prod
        
def check_args(args, len_, caller=''):
    if len(args) < len_:
        panic('Too few args Caller: %s' % caller)
        return False
    return True
        
def sub(args):
    if check_args(args, 2):
        diff = eval_(args[0])
        for i in args[1:]: diff -= eval_(i)
        return diff
        
def gt(args):
    if check_args(args, 2):
        return args[0] > args[1]
                    
        
def inp(args):
    return raw_input()
        
def atoi(args):
    if not isinstance(args, list): return int(eval(args))
    if len(args) != 1:
        panic("incorrect # of arguments")
    else:
        return int(eval(args[0]))
   
def def_func(args):
    return Function(args[0], args[1])



def eq(args):
    if check_args(args, 2):
        return args[0] == args[1]    
    
def lt(args):
    if check_args(args, 2):
        return args[0] < args[1]    

def set_var(args):
    global_env[args[0].tosexp()] = eval_(args[1])
    return 'var %s = %s' % (args[0].tosexp(), eval_(args[1])) 
        
def pyeval(args):
    return eval(args[0])

def range_(args):
    if check_args(args, 2):
        return range(args[0], args[1] + 1)

def cond(args):
    if len(args) < 3:
        panic("Too few arguments to if")
    else:
        if eval_(args[0]):
            return eval_(args[1])
        else: return eval_(args[2])
        
def get_var(args):
    if args[0].tosexp() in global_env:
        return global_env[eval_(args[0].tosexp())]
 

defined_macros = {
                    Symbol('out'):out, Symbol('+'):add,
                    Symbol('-'):sub, Symbol('*'):mul,
                    Symbol('/'):div, Symbol('in'):inp,
                    Symbol('atoi'):atoi, Symbol('fst'):l.fst,
                    Symbol('set'):set_var, Symbol('pyeval'):pyeval,
                    Symbol('if'):cond, Symbol('>'):gt,
                    Symbol('get'):get_var, Symbol('..'): range_,
                    Symbol('='):eq, Symbol('<'):lt,
                    Symbol('sqrt'):sqrt_, Symbol('sq'):sq,
                    Symbol('pi'):pi, Symbol('++'):l.sum_,
                    Symbol('abs'):abs_, Symbol('get'):get_var,
                    Symbol('fun'):def_func, Symbol('even'):even,
                    Symbol('odd'):odd, Symbol('prime'):is_prime,
                    Symbol('panic'):panic_, Symbol('tail'):l.tail
                    }
def call_func(func, args):
    return func.call(args)

def is_atom(it):
    return not isinstance(it, list)

def eval_(exp):
    for m in defined_macros:
        if not is_atom(exp):
            if exp[0] == m:
                return defined_macros[m](exp[1:])
    if not is_atom(exp) and hasattr(exp[0], 'tosexp') and isinstance(global_env[exp[0].tosexp()], Function):
        return call_func(global_env[exp[0].tosexp()], exp[1:])
    return exp
