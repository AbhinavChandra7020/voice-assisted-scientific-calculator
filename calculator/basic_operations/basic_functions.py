import math
from ..utils.angle_modes import angle_mode

# trigonometric functions with degrees
def sin(x):
    return math.sin(angle_mode.to_radians(x))

def cos(x):
    return math.cos(angle_mode.to_radians(x))

def tan(x):
    return math.tan(angle_mode.to_radians(x))

def asin(x):
    return angle_mode.from_radians(math.asin(x))

def acos(x):
    return angle_mode.from_radians(math.acos(x))

def atan(x):
    return angle_mode.from_radians(math.atan(x))

def cbrt(x):
 
    if x >= 0:
        return x ** (1/3)
    else:
        return -((-x) ** (1/3))

def nthroot(x, n):

    n = int(n)
    if n == 0:
        raise ValueError("Cannot calculate 0th root")
    
    if x >= 0:
        return x ** (1/n)
    else:
        if n % 2 == 1:  
            return -((-x) ** (1/n))
        else:  
            return complex(x) ** (1/n)

def root(x, n):
    return nthroot(x, n)

FUNCTIONS = {
    # trigonometric 
    'sin': sin,
    'cos': cos,
    'tan': tan,
    'asin': asin,
    'acos': acos,
    'atan': atan,
    
    # logarithmic
    'log': math.log10,
    'ln': math.log,
    'log2': math.log2,
    
    # exponential and roots
    'exp': math.exp,
    'sqrt': math.sqrt,
    'cbrt': cbrt,
    'cuberoot': cbrt,  
    'nthroot': nthroot,
    'root': root,
    
    # other
    'abs': abs,
    'factorial': math.factorial,
    'floor': math.floor,
    'ceil': math.ceil,
    'round': round,


}

def get_function(name):
    if name in FUNCTIONS:
        return FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown function: {name}")