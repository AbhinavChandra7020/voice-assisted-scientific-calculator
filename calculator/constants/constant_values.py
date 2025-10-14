import math

CONSTANTS = {
    'pi': math.pi,
    'e': math.e,
    'tau': math.tau,
    'j': 1j,  
    'i': 1j,  
    'phi': (1 + math.sqrt(5)) / 2,  
    'golden_ratio': (1 + math.sqrt(5)) / 2,  
}

def get_constant(name):

    if name.lower() == 'ans':
        from ..parser import get_ans
        return get_ans()
    
    if name in CONSTANTS:
        return CONSTANTS[name]
    else:
        raise ValueError(f"Unknown constant: {name}")