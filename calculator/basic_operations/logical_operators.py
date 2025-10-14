# basic logical operations
def logical_and(a, b):

    return 1 if (a and b) else 0

def logical_or(a, b):

    return 1 if (a or b) else 0

def logical_not(a):

    return 0 if a else 1

def logical_xor(a, b):

    return 1 if bool(a) != bool(b) else 0

# extended logical operations
def logical_nand(a, b):

    return 1 if not (a and b) else 0

def logical_nor(a, b):

    return 1 if not (a or b) else 0

def logical_xnor(a, b):

    return 1 if bool(a) == bool(b) else 0

def implies(a, b):

    return 1 if (not a or b) else 0

# comparison operators
def equals(a, b, tolerance=1e-10):

    return 1 if abs(a - b) < tolerance else 0

def not_equals(a, b, tolerance=1e-10):

    return 0 if abs(a - b) < tolerance else 1

def greater_than(a, b):

    return 1 if a > b else 0

def less_than(a, b):

    return 1 if a < b else 0

def greater_equal(a, b):
  
    return 1 if a >= b else 0

def less_equal(a, b):
 
    return 1 if a <= b else 0


LOGICAL_FUNCTIONS = {
    # Short 'l' prefix as python alredy has and, not, or, etc
    'land': logical_and,
    'lor': logical_or,
    'lnot': logical_not,
    'lxor': logical_xor,
    
    # CAPS
    'AND': logical_and,
    'OR': logical_or,
    'NOT': logical_not,
    'XOR': logical_xor,
    
    'logic_and': logical_and,
    'logic_or': logical_or,
    'logic_not': logical_not,
    'logic_xor': logical_xor,
    
    # extended logical operations
    'NAND': logical_nand,
    'nand': logical_nand,
    'NOR': logical_nor,
    'nor': logical_nor,
    'XNOR': logical_xnor,
    'xnor': logical_xnor,
    'IMPLIES': implies,
    'implies': implies,
    
    # comparison operations
    'eq': equals,
    'neq': not_equals,
    'gt': greater_than,
    'lt': less_than,
    'gte': greater_equal,
    'lte': less_equal,
    'equals': equals,
    'not_equals': not_equals,
    'greater': greater_than,
    'less': less_than,
}

def get_function(name):
    if name in LOGICAL_FUNCTIONS:
        return LOGICAL_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown logical function: {name}")