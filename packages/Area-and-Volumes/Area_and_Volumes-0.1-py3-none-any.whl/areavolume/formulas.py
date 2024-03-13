import math
import mpmath

def square(l):
    l = float(l)
    return l ** 3

def rectangle(l, h):
    l, w = float(l), float(w)
    return l * w

def circle(r):
    r = float(r)
    return math.pi * r ** 2

def triangle(b, h):
    b, h = float(b), float(h)
    return (b * h) / 2

def pentagon(sl):
    sl = float(sl)
    return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * sl

def hexagon(sl):
    sl = float(sl)
    return (3 * math.sqrt(3)) / 2 * sl ** 2

def heptagon(sl):
    sl = float(sl)
    return (7/4) * sl ** 2 * mpmath.cot(math.pi / 7)

def octagon(sl):
    sl = float(sl)
    return 2 * (1 + math.sqrt(2)) * sl ** 2

def nonagon(sl):
    sl = float(sl)
    return (9/4) * sl ** 2 * mpmath.cot(math.pi / 9)

def decagon(sl):
    sl = float(sl)
    return (5/2) * sl ** 2 * math.sqrt(5 + 2 * math.sqrt(5))

def cube(l):
    l = float(l)
    return l ** 3

def rectangular_prism(l, w, h):
    l, w, h = float(l), float(w), float(h)
    return l * w * h

def sphere(r):
    r = float(r)
    return (4/3) * math.pi * r ** 3

def cylinder(r, h):
    r, h = float(r), float(h)
    return math.pi * r ** 2 * h

def cone(r, h):
    r, h = float(r), float(h)
    return math.pi * r ** 2 * h / 3

def dodecahedron(el):
    el = float(el)
    return (15 + 7 * math.sqrt(5)) / 4 * el ** 3

def triangular_prism(b, h):
    b, h = float(b), float(h)
    return (1/3) * b * h

def hemisphere(r):
    r = float(r)
    return (2/3) * math.pi * r ** 3

def torus(MinR, MajR):
    MinR, MajR = float(MinR), float(MajR)
    return math.pi * MinR ** 2 * (2 * math.pi * MajR)

def rhombicosidodecahedron(el):
    el = float(el)
    return (el ** 3 * (60 + 29 * math.sqrt(5))) / 3
