#!/usr/bin/env python3

"""
Basic vector plot module implementation with numpy and matplotlib.pyplot
module implement 2 objects : Point, Vect, that can be drawn and can interact each others

Examples :
    1)
    Point((0,2)) => Point([0,2])
    Vect(Point((0,6))) => Vect([0,6])
    2)
    Point((1,6), name='B') => Point([1,6])
    Point((0,3), name='A') => Point([0,3])
    Vect('B', start='A') => Vect([1,3])
    3)
    2*Vect([1,2]) + Vect([2,-1]) = Vect([3,1])
    2*Vect([1,2]) + Vect([2,-1]) + Point([3,0]) = Point([7,1])
"""

import re

import numpy as np
#import pandas as pd
from matplotlib import pyplot as plt


def inccrement_point_name(name):
    if len(name) == 1:
        return name + '1'
    return name[0] + str(int(name[1]) + 1)

def gen_name(liste):
    """
    A name generator for Point and Vect

    Args:
        liste (string) : an iterable containing names to give
    Returns:
        A generator
    """
    index = 0
    while True:
        for lettre in liste:
            yield lettre + str(index)
        index += 1

class Point:
    """
    An object that represent a point

    Args:
        pos (tuple): point position
        name (str): should be [A-Z] or [A-Z][0-9]
        is_saved (bool): don't save the instance
        is_show (bool): plot at creation
    Returns:
        Point object
    """
    # store created intances with is_saved flag
    instances = {}
    # name generator
    get_name = gen_name('GHIJKLMNOPQRSTUVWXYZABCDEF')

    def __init__(self, pos=(0,0), name=None, is_saved=True, show=True):

        self.x, self.y = self.val = np.array(pos)

        if self in Point.instances.values(): # Point already exist (same val): don't save it
            is_saved = False

        self.set_name(name)

        self.is_show = False # will be toggled

        if is_saved:
            if show:
                self.toggle_plot()
            Point.instances[self.name] = self

    def rename(self, name):
        if not Point.iS_good_name(name):
            return
        del Point.instances[self.name]
        Point(self.val, name)
        #del Point.instances[self.name]


    def copy(self):
        """ non instance-saved copy """
        return Point(self.val, name=self.name, is_saved=False)

    def set_name(self, name):
        """ Set name to attribute, generate one if needed"""
        if name == None or not Point.iS_good_name(name):
            self.name = next(Point.get_name)
            while self.name in Point.instances.keys():
                self.name = next(Point.get_name)
        else :
            self.name = name

    @staticmethod
    def iS_good_name(name):
        """ Compare name to regex, should be "[A-Z]" or "[A-Z][0-9]" """
        if isinstance(name,str):
            if re.fullmatch('[A-Z]\d|[A-Z]', name) != None:
                return True
        print('Point name format should be "[A-Z]" or "[A-Z][0-9]"\nGive 1 4 U!')
        return False

    #def __getitem__(self, k):
    #    return self.val[k]

    def __repr__(self):
        return 'Point({})'.format(self.val)

    def __eq__(self, other):
        try :
            if all(other.val == self.val):
                return True
        except Exception as err :
            print("Should be compared to a point")
            print(err)
        return False

    def toggle_plot(self):
        """ toggle object display on the graph """
        if self.is_show:
            self.graph.remove()
            self.graph_text.remove()
        else:
            self.graph = ax.scatter(self.x, self.y)
            self.graph_text = ax.annotate(self.name, self.val*1.05)
        self.is_show = not self.is_show


    def transform(self, vect):
        """
        give an image of the point by vect translation
        Args:
            vect (Vect): translation vector
        Returns
            a new Point object
        """
        print(vect)
        val = vect.val + self.val
        temp_point = Point(pos=val, is_saved=False)
        if temp_point in Point.instances.values():
            k = [k for k,v in Point.instances.items() if v == temp_point][0]
            print(f'limage de {self.name} par le Vect {vect.name} est {k}')
            return Point.instances[k]
        return Point(val, inccrement_point_name(self.name))

    def __del__(self):
        print('suppression du point {}'.format(self.name))
        try :
            self.graph.remove()
            self.graph_text.remove()
        except AttributeError:
            print('Point {} has no graph plotted'.format(self.name))

def parse_point(A):
    """ parse a string, tuple or Point into Point object """
    try :
        if isinstance(A, Point):
            return A.copy()
        elif isinstance(A, str):
            return Point.instances[A].copy()
        elif isinstance(A, tuple):
            return Point(A, is_saved=False)
    except Exception as err :
        print(A)
        print(err)

class Vect:
    """
    An object that represent a vector between Point object A and B

    Args:
        end (Point): vector end
        start (Point): vector start
        is_saved (bool): save object in instances dict
        show (bool): diplay on graph at creation
    Returns
        Vect object
    """

    # store created intances with is_saved flag
    instances = {}
    # name generator
    get_name = gen_name('uvwxyzabcdefghijklmnopqrst')

    def __init__(self, end, start=Point((0,0),is_saved=False), name=None, is_saved=True, show=False):

        A, B = map(parse_point, [start, end])

        self.val = B.val - A.val
        self.start = A
        self.set_name(name)
        self.is_show = False

        if show:
            self.toggle_plot()
        Vect.instances[self.name] = self

    def __repr__(self):
        return 'Vect({})'.format(self.val)

    def set_name(self, name):
        """ Generate a new name if given isn"t right """
        if name == None or not Vect.iS_good_name(name):
            self.name = next(Vect.get_name)
            while self.name in Vect.instances.keys():
                self.name = next(Vect.get_name)
        else :
            self.name = name

    @staticmethod
    def iS_good_name(name):
        """ Test name format : should be [a-z] or [a-z][0-9] """
        if isinstance(name,str):
            if re.fullmatch('[a-z]\d|[a-z]', name) != None:
                return True
        print('Vect name format should be "[a-z]" or "[a-z][0-9]"\nGive 1 4 U!')
        return False

    def toggle_plot(self):
        """ toggle object diplay on graph """
        if self.is_show:
            self.graph.remove()
        else:
            A, B = self.start.val, self.val
            self.graph = ax.arrow(A[0], A[1], B[0], B[1], head_width=0.2)
        self.is_show = not self.is_show

    @property
    def norm(self):
        return np.sqrt(np.sum((self.val)**2))

    def __add__(self, A):
        if isinstance(A, Vect):
            return Vect(Point(self.val + A.val))
        elif isinstance(A, Point):
            return Point(self.val + A.val)

    def __radd__(self, A=(0,0)):
        if isinstance(A, Vect):
            return Vect(Point(self.val + A.val))
        elif isinstance(A, Point):
           return Point(self.val + A.val)

    def __sub__(self, A=(0,0)):
        if isinstance(A, Vect):
            return Vect(Point(self.val - A.val))
        elif isinstance(A, Point):
           return Point(self.val - A.val)

    def __rsub__(self, A=(0,0)):
        if isinstance(A, Vect):
            return Vect(Point(A.val - self.val))
        elif isinstance(A, Point):
           return Point(A.val - self.val)

    def __mul__(self, n=1):
        return Vect(Point(self.val*n))

    def __rmul__(self, n=1):
        return Vect(Point(self.val*n))

    def __truediv__(self, n=1):
        return Vect(Point(self.val/n))

    def __getitem__(self, k):
        return self.val[k]

    def __del__(self):
        print('suppression du Vect {}'.format(self.name))
        try:
            self.graph.remove()
        except AttributeError :
            print('Vect {} has no graph attribute'.format(self.name))


# Init plot





if __name__=='__main__':
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
    if False: # example1
        for n in 'AB':
            Point(pos=np.random.randint(1,9,2), name=n)
        input("\nrunning : \"u = Vect('B', start='A')\" , press enter!")
        u = Vect('B', start='A')
        input("\nrunning : \"u.toggle_plot()\" , press enter!")
        u.toggle_plot()
        input("\nrunning : \"E = Point((4,5),name='E')\" , press enter!")
        E = Point((4,5),name='E')
        input("\nrunning : \"E.transform(u)\" , press enter!")
        E2 = E.transform(u)
        input("\nrunning : \"E2.toggle_plot()\" , press enter!")
        E2.toggle_plot()
        input("\nrunning : \"E2.toggle_plot()\" , press enter!")
        E2.toggle_plot()
        input("\nrunning : \"v = Vect((2,3), name='v').toggle_plot()\" , press enter!")
        v = Vect((2,3), name='v')
        input("\nrunning : \"E3 = 2*v - u/2 + E2\" , press enter!")
        E3 = 2*v - u/2 + E2
        input("\nrunning : \"w = 2*v - u/2\" , press enter!")
        w = 2*v - u/2
        input("\nrunning : \"w.start = E2\" , press enter!")
        w.start = E2
        input("\nrunning : \"w.toggle_plot()\" , press enter!")
        w.toggle_plot()

    if False:
        for n in 'AB':
            Point(pos=np.random.randint(1,9,2), name=n)
        input("running : \"u = Vect((1,2))\" , press enter!")
        u = Vect((1,2))
        input("\nrunning : \"Point.instances['A'].transform(u)\" , press enter!")
        Point.instances['A'].transform(u)
        input("\nrunning : \"u = Vect('B', start='A', show=True )\" , press enter!")
        v = Vect('B', start='A', show=True)
        input("\nrunning : \"Point.instances['A'].transform(v)\" , press enter!")
        Point.instances['A'].transform(v)
        #input("\nrunning : \"\" , press enter!")
        #input("\nrunning : \"\" , press enter!")
        #input("\nrunning : \"\" , press enter!")

    if True:
        A = Point(pos=np.random.randint(1,9,2), name='A')
        B = Point(pos=np.random.randint(1,9,2), name='B')




