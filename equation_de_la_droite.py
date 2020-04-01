#!/usr/bin/env python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.ion()



data = {'A' : (2,3),
        'B' : (4,6),
        'C' : (3,7)}

df = pd.DataFrame(data.values(),
                  index=data.keys(),
                  columns=('x', 'y'))

fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.scatter(df.x, df.y)
[ax.annotate(d.name, d.to_numpy()*1.1) for d in [df.iloc[i] for i in range(len(df))]]
#ax.text(df.x * (1 + 0.01), df.y * (1 + 0.01) , df.index, fontsize=12)
#(ax.annotate(s, tuple(xv)
ax.set_xticks(np.arange(11))
ax.set_yticks(np.arange(11))
plt.xlim(0,10)
plt.ylim(0,10)
plt.grid()
plt.show()

def gen_vector():
    vector_dct={}

    def p(pt):
        return df.loc[pt].to_numpy()

    def vector(s):
        A=p(s[0])
        B=p(s[1])
        #n = sA+sB
        if s in vector_dct.keys():
            print('le vecteur {} est déjà tracé')
            return None
        print('new {} vector'.format(s))
        AB = ax.arrow(A[0],A[1],B[0]-A[0], B[1]-A[1], head_width=0.2)
        vector_dct[s] = AB

    def del_vector(AB):
        vector_dct[AB].remove()
        del vector_dct[AB]

    return vector, del_vector

vector, del_vector = gen_vector()

def create_vector(s='AB'):
    vector_dct = {}
    print(vector_dct)

def p(pt):
    return df.loc[pt].to_numpy()

class Point:
    instances = {}

    def __init__(self, *args, **kwargs):
        pass

class Vect:
    instances = {}

    def __init__(self, s):

        if s in Vect.instances.keys() :
            print('le vecteur {} existe déjà!')
        #    return
           # return Vect.instances[s]
        print('ce code est excécuté')

        self.s = s
        A=p(s[0])
        B=p(s[1])
        self.A = A
        self.B = B
        self.AB = ax.arrow(A[0],A[1],B[0]-A[0], B[1]-A[1], head_width=0.2)

        Vect.instances[s] = self.AB

    def __del__(self):

        print('suppression du vecteur {}'.format(self.s))
        self.AB.remove()
        del Vect.instances[self.s]

    @property
    def xy(self):
        return self.A

    @property
    def norm(self):
        return np.sqrt((self.B-self.A)**2)

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

    def __getitem__(self, k):
        return self.val[k]











