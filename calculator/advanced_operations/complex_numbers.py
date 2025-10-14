import cmath  
import math

def complex_from_parts(real, imag):

    return complex(real, imag)

def real_part(z):

    return z.real

def imag_part(z):
    
    return z.imag

def conjugate(z):
    
    return z.conjugate()

def abs_complex(z):
    
    return abs(z)

def arg(z):
    
    return cmath.phase(z)

def polar_to_rect(r, theta):
    
    return cmath.rect(r, theta)

def rect_to_polar(z):
    
    return cmath.polar(z)

def csqrt(z):
    
    return cmath.sqrt(z)

def cexp(z):
    
    return cmath.exp(z)

def clog(z):
    
    return cmath.log(z)

def csin(z):
    
    return cmath.sin(z)

def ccos(z):
    
    return cmath.cos(z)

def ctan(z):
    
    return cmath.tan(z)

COMPLEX_FUNCTIONS = {
    # construction and parts
    'complex': complex_from_parts,
    'real': real_part,
    'imag': imag_part,
    'conj': conjugate,
    'conjugate': conjugate,
    
    # polar operations
    'abs': abs_complex,
    'arg': arg,
    'phase': arg,  
    'polar': rect_to_polar,
    'rect': polar_to_rect,
    
    # complex math functions
    'csqrt': csqrt,
    'cexp': cexp,
    'clog': clog,
    'csin': csin,
    'ccos': ccos,
    'ctan': ctan,
}

def get_function(name):
    if name in COMPLEX_FUNCTIONS:
        return COMPLEX_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown complex function: {name}")