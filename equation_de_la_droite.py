#!/usr/bin/env python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.ion()



fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xticks(np.arange(11))
ax.set_yticks(np.arange(11))
plt.xlim(0,10)
plt.ylim(0,10)
plt.grid()
plt.show()

class Point:
    instances = {}

    def __init__(self, pt={'A' : (0,0)}):
        self.name = [k for k in pt.keys()][0]
        self.val = np.array(pt[self.name])
        self.x, self.y = pt[self.name]

        self.graph = ax.scatter(self.x, self.y)
        ax.annotate(self.name, np.array(self.val)*1.05)
        Point.instances[self.name] = self

    def __getitem__(self, k):
        return self.val[k]

    def __repr__(self):
        return 'Point({})'.format(self.val)

    def __add__(self, A=(0,0)):
        return self.val + A[:]

    def __radd__(self, A=(0,0)):
        print(self.val)
        print(A[:])
        return self.val + A[:]

    def __sub__(self, A=(0,0)):
        return self.val - A[:]

    def __rsub__(self, A=(0,0)):
        return A[:] - self.val

    def remove(self):
        self.graph.remove()
        del Point.instances[self.name]

    def __del__(self):

        print('suppression du point {}'.format(self.name))
        self.graph.remove()
        del Point.instances[self.name]

class Vect:
    instances = {}

    def p(pt):
        return df.loc[pt].to_numpy()

    def __init__(self, A, B):
        """ créé un vecteur de A vers B, avec A et B des instances de Point """

        self.s = A.name + B.name
        if self.s in Vect.instances.keys() :
            print('le vecteur {} existe déjà!'.format(self.s))

        self.A = A.val
        self.B = B.val
        self.graph = ax.arrow(A[0],A[1],B[0]-A[0], B[1]-A[1], head_width=0.2)

        Vect.instances[self.s] = self

    def remove(self):
        self.graph.remove()
        del Vect.instances[self.s]

    def __del__(self):

        print('suppression du vecteur {}'.format(self.s))
        self.graph.remove()
#        del Vect.instances[self.s]
        #self.__del__()

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
        return str(self.B - self.A)

    def __add__(self, A=(0,0)):
        return self.val + A[:]

    def __radd__(self, A=(0,0)):
        return self.val + A[:]

    def __sub__(self, A=(0,0)):
        return self.val - A[:]

    def __rsub__(self, A=(0,0)):
        return A[:] - self.val

    def __mul__(self, n=1):
        return self.val*n

    def __rmul__(self, n=1):
        return self.val*n

    def __truediv__(self, n=1):
        return self.val/n




    def __getitem__(self, k):
        return self.val[k]


#data = {'A' : (2,3),
#        'B' : (4,6),
#        'C' : (3,7)}
#
#for k, v in data.items() :
#    Point({k:v})
#
#A = Point.instances['A']
#B = Point.instances['B']
#C = Point.instances['C']

for n in 'ABC':
    Point({n:np.random.randint(1,9,2)})
p = Point.instances
v = Vect.instances

plt.show()







