#!/usr/bin/env python3

import re

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.ion()

fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xticks(np.arange(0,11,1))
ax.set_yticks(np.arange(0,11,1))
plt.xlim(0,10)
plt.ylim(0,10)
plt.grid()
plt.show()

def iS_good_name(name):
    if isinstance(name,str):
        if re.fullmatch('[A-Z]\d|[A-Z]', name) != None:
            return True
    print('Point name format should be "[A-Z]" or "[A-Z][0-9]"')
    print('Give one for U!')
    return False

def inccrement_point_name(name):
    if len(name) == 1:
        return name + '1'
    return name[0] + str(int(name[1]) + 1)
               
def gen_name(liste):
    index = 0
    while True:
        for lettre in liste:
            yield lettre + str(index)
        index += 1
class Point:
    instances = {}
    get_name = gen_name('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
           
    def __init__(self, pos=(0,0), name=None, is_temp = False):
        
        self.x, self.y = self.val = np.array(pos)
        
        if name == None or not iS_good_name(name):
            self.name = next(Point.get_name)
        else :
            self.name = name

        self.is_show = False
        if not is_temp: 
            self.toggle_plot()
            Point.instances[self.name] = self

    def __getitem__(self, k):
        return self.val[k]

    def __repr__(self):
        return 'Point({})'.format(self.val)
    
    def __eq__(self, other):
        try :
            if all(other.val == self.val):
                return True            
        except Exception as err :
            print("Should be compare to a point")
            print(err)
        return False
                
    def toggle_plot(self):
        if self.is_show:
            self.graph.remove()
            self.graph_text.remove()
        else:
            self.graph = ax.scatter(self.x, self.y)
            self.graph_text = ax.annotate(self.name, self.val*1.05)
        self.is_show = not self.is_show            
                

    def transform(self, vecteur):
        val = vecteur.val + self.val
        temp_point = Point(pos=val, is_temp=True)
        if temp_point in Point.instances.values():
        #if any(list(map(lambda x : all(x.val == val), [a for a in Point.instances.values()]))):
            #k = [k for k,v in Point.instances.items() if all(v.val==val)][0]
            k = [k for k,v in Point.instances.items() if v == temp_point][0]
            print(f'limage de {self.name} par le vecteur {vecteur.name} est {k}')
            return Point.instances[k]
        return Point(val, inccrement_point_name(self.name))

    def plot(self, *args):
        to = self.transform(*args)
        Vect(self, to)

    def remove(self):
        self.graph.remove()
        self.graph_text.remove()
        del Point.instances[self.name]

    def __del__(self):

        print('suppression du point {}'.format(self.name))
        self.graph.remove()
        self.graph_text.remove()
        del Point.instances[self.name]


def vect2(*args):
    try :
        print('len : ', len(args))
        if len(args) > 1:
            if all([isinstance(a, Point) for a in args]):
                print('Point')
                A, B = [a.val for a in args]
            elif all([isinstance(a, tuple) for a in args]):
                print('double tuple')
                A, B = [np.array(a) for a in args]
        elif isinstance(args[0], np.ndarray):
            print('numpy')
            A = np.array([0,0])
            B = args[0]
        elif isinstance(args[0], tuple):
            print('tuple')
            A, B = [np.array(a) for a in [(0,0), args[0]]]
        elif isinstance(args[0], str):
            print('str')
            A, B = [Point.instances[v].val for v in args[0]]

        return B - A
    except Exception as err :
        print(args)
        print(err)
        

def vectorize(A):
    try :
        if isinstance(A, Point):
            return A.Val, A.name
        elif isinstance(A, str):
            return Point.instances[A].val, A
        elif isinstance(A, tuple):
            return np.array(A), None
    except Exception as err :
        print(args)
        print(err)

class Vect:
    instances = {}

    #def p(pt):
    #    return df.loc[pt].to_numpy()
    def get_name():
        names = 'abcdefghijklmnopqrstuvwxyz'
        for name in names:
            yield name

    def __init__(self, *args, start=(0,0), is_temp=False):
        """ créé un vecteur de A vers B, avec A et B des instances de Point """

        if len(args) == 2:
            self.A, A_name = vectorize(args[0])
            self.B, B_name = vectorize(args[1])
        elif len(args) == 1:
            self.A = np.array(start)
            self.B, B_name = vectorize(args[0])
            
        self.val = self.B - self.A
        self.name = (get_name())
        
        self.A = start
        self.B = end
        
        if self.name in Vect.instances.keys() :
            print('le vecteur {} existe déjà!'.format(self.name))

        self.A = A.val
        self.B = B.val
        self.graph = ax.arrow(A[0],A[1],B[0]-A[0], B[1]-A[1], head_width=0.2)

        Vect.instances[self.name] = self

    def remove(self):
        self.graph.remove()
        del Vect.instances[self.name]

    def __del__(self):

        print('suppression du vecteur {}'.format(self.name))
        self.graph.remove()
#        del Vect.instances[self.name]
        #self.__del__()

    @staticmethod
    def image(A, BC):
        """ image du point A (class Point) par BC (class Vect) """
        return Point({A.s + '1': A+BC})

    @property
    def start(self):
        return self.A

    @property
    def end(self):
        return self.B

    @property
    def norm(self):
        return np.sqrt(np.sum((self.B-self.A)**2))

    @property
    def val(self):
        return self.B - self.A

    def __repr__(self):
        return 'Vect({})'.format(self.B - self.A)

    def __add__(self, A=(0,0)):
        val = self.val + A[:]
        return self.val + A[:]

    def __radd__(self, A=(0,0)):
        return self.val + A[:]

    def __sub__(self, A=(0,0)):
        return tuple(self.val - A[:])

    def __rsub__(self, A=(0,0)):
        return tuple(A[:] - self.val)

    def __mul__(self, n=1):
        return tuple(self.val*n)

    def __rmul__(self, n=1):
        return tuple(self.val*n)

    def __truediv__(self, n=1):
        return tuple(self.val/n)

    def __getitem__(self, k):
        return self.val[k]


for n in 'ABCD':
    Point(pos=np.random.randint(1,9,2), name=n)

plt.show()


#Vect(p['B'], p['C'])
#Vect(p['B'], p['A'])
#a= v['BC'] + v['BA']

def parse(formule):
    formule = re.sub('\s','', formule)
    val = re.split('[+-/\*]', formule)
    maths = re.sub('\w','',formule)
    maths = list(maths)
    #maths = re.split('[\w]', maths)
    print('val : ', val)
    print('maths : ', maths)
    def go(name):
        if len(name)>1:
            if re.match('\d', name[1]) != None:
                return p[name]
            else :
                return v[name]
        else:
            if re.match('\d', name) != None:
                return int(name)
            else:
                return p[name]

    for sign in ['/','*','+','-']:
        if not maths:
            break
        for i,m in enumerate(maths):
            print(val[i],m,val[i+1])
            if m == '/':
                res = go(val[i])/go(val[i+1])
            elif m == '*':
                res = go(val[i])*go(val[i+1])
            elif m == '+':
                res = go(val[i])+go(val[i+1])
            elif m == '-':
                res = go(val[i])-go(val[i+1])

            del val[i:i+2]
            val.insert(i, res)
            del maths[i]

    return val
#    res = get_obj(val.pop(0))
#    while val:
#        print('lenght: val : {} , math : {}'.format(len(val), len(maths)))
#        calc = maths.pop(0)
#        print('--')
#        print(calc)
#
#        if calc == '+':
#            print('+')
#            res = res + get_obj(val.pop(0))
#        elif calc == '-':
#            res = res - get_obj(val.pop(0))
#        elif calc == '/':
#            res = res / get_obj(val.pop(0))
#        elif calc == '*':
#            res = res * get_obj(val.pop(0))
#
#
#    return res




