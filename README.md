# VectorObject
### Purpose
Draw and manipulation basic vectorial representation with python3 and matplotlib lib

just vecteur.py file is usefull, others are expermientals

### Functionalities 
it implement two class:
  - Point : a point (that's make sense, don't you think?)
  - Vect : really? You don't get it? 
  
you can toggle object display 
and perform simple calculation like
  - Vect + Vect => Vect
  - Vect + Point => Point
  - n*Vect => Vect

and others

### Usage
Module
```python
from vecteur import get_vect_n_point_class
fig, ax = matplotlib.pyplot.subplots()
Point, Vect = get_vect_n_point_class(ax)
```

Run example
```bash
python3
import example
```

Help :
```python
import vecteur
help(vecteur)
```



