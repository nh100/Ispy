'''
Created on Jul 16, 2013

@author: noah
'''


from sexpdata import Symbol, loads
from main import *

                
def run():
    if len(sys.argv)>1:
        with open('test.isp') as f:
            for line in f: eval_(loads(line))
    else:
        print '''
            --------------------
            Ispy Interpreter v'''+str(VERSION)+'''
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
