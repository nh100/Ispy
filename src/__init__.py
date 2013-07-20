'''
Created on Jul 16, 2013

@author: noah
'''


from sexpdata import Symbol, loads
import sys
import mathlib

global_env = {}
VERSION = 0.1
class Panic(object):
    msg = ''
    def __init__(self, s):
        self.msg = s
    def __str__(self):
        return 'Panic: %s' % self.msg
        
def panic(s):
            sys.stderr.write(str(Panic(s)))
            
def out(args):
    if check_args(args, 1):
        for v in args: sys.stdout.write(str(eval_(v)))
    return ''
        
def add(args):
    if check_args(args, 2):
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
        
def fst(args):
    if not isinstance(args[0], list):
        panic("argument not list")
    else: return eval_(args[0][0])

def eq(args):
    if check_args(args, 2):
        return args[0] == args[1]    
    
def lt(args):
    if check_args(args, 2):
        return args[0] < args[1]    

def set_var(args):
    global_env[args[0]] = args[1]
    print global_env
    return global_env[args[0]]
        
def pyeval(args):
    return eval(args[0])
        
def cond(args):
    if len(args) < 3:
        panic("Too few arguments to if")
    else:
        if eval_(args[0]):
            return eval_(args[1])
        else: return eval_(args[2])
        
def get_var(args):
    if Symbol(args[0]) in global_env:
        return global_env[Symbol(args[0])]
        
defined_macros = {
                    Symbol('out'):out, Symbol('+'):add,
                    Symbol('-'):sub, Symbol('*'):mul,
                    Symbol('/'):div, Symbol('in'):inp,
                    Symbol('atoi'):atoi, Symbol('fst'):fst,
                    Symbol('set'):set_var, Symbol('pyeval'):pyeval,
                    Symbol('if'):cond, Symbol('>'):gt,
                    Symbol('get'):get_var, Symbol('pi'):mathlib.pi,
                    Symbol('='):eq, Symbol('<'):lt                 
                    }
        
def is_atom(it):
    return not isinstance(it, list)
        
def eval_(exp):
    for m in defined_macros:
        if not is_atom(exp):
            if exp[0] == m:
                return defined_macros[m](exp[1:])
    return exp
                
def run():
    if len(sys.argv)>1:
        with open('test.isp') as f:
            for line in f: eval_(loads(line))
    else:
        print '''
            --------------------
            Isp Interpreter v'''+str(VERSION)+'''
            --------------------'''
        while True:
            sys.stdout.write("?> ")
            input = raw_input()
            input = input.replace('[', '(')
            input = input.replace(']', ')')
            if not input: break
            if input.split()[0] == "'": continue
            print(str(eval_(loads(input, true='true', false='false'))))
       



if __name__ == '__main__':
    run()
