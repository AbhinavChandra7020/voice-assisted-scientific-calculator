import math

def is_vector(obj):
    if not isinstance(obj, list):
        return False
    if len(obj) == 0:
        return False
    return all(isinstance(x, (int, float, complex)) for x in obj)

def validate_same_dimension(v1, v2, operation="operation"):
    if len(v1) != len(v2):
        raise ValueError(f"Vectors must have same dimension for {operation}")

def vector(*components):

    return list(components)

def magnitude(v):

    return math.sqrt(sum(x**2 for x in v))

def normalize(v):

    mag = magnitude(v)
    if mag == 0:
        raise ValueError("Cannot normalize zero vector")
    return [x / mag for x in v]

def dot(v1, v2):

    validate_same_dimension(v1, v2, "dot product")
    return sum(a * b for a, b in zip(v1, v2))

def cross(v1, v2):

    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product requires 3D vectors")
    
    x = v1[1] * v2[2] - v1[2] * v2[1]
    y = v1[2] * v2[0] - v1[0] * v2[2]
    z = v1[0] * v2[1] - v1[1] * v2[0]
    
    return [x, y, z]

def angle_between(v1, v2, degrees=False):

    validate_same_dimension(v1, v2, "angle calculation")
    
    dot_product = dot(v1, v2)
    mag1 = magnitude(v1)
    mag2 = magnitude(v2)
    
    if mag1 == 0 or mag2 == 0:
        raise ValueError("Cannot calculate angle with zero vector")
    
    cos_angle = max(-1, min(1, dot_product / (mag1 * mag2)))
    angle_rad = math.acos(cos_angle)
    
    if degrees:
        return math.degrees(angle_rad)
    return angle_rad

def projection(v1, v2):

    dot_product = dot(v1, v2)
    v2_squared = dot(v2, v2)
    
    if v2_squared == 0:
        raise ValueError("Cannot project onto zero vector")
    
    scalar = dot_product / v2_squared
    return [scalar * x for x in v2]

def distance(v1, v2):

    validate_same_dimension(v1, v2, "distance calculation")
    diff = [a - b for a, b in zip(v1, v2)]
    return magnitude(diff)

def scalar_multiply(v, scalar):

    return [x * scalar for x in v]

def add_vectors(v1, v2):

    validate_same_dimension(v1, v2, "addition")
    return [a + b for a, b in zip(v1, v2)]

def subtract_vectors(v1, v2):

    validate_same_dimension(v1, v2, "subtraction")
    return [a - b for a, b in zip(v1, v2)]

def unit_x():
    return [1, 0, 0]

def unit_y():
    return [0, 1, 0]

def unit_z():
    return [0, 0, 1]

VECTOR_FUNCTIONS = {
    'vector': vector,
    'unit_x': unit_x,
    'unit_y': unit_y,
    'unit_z': unit_z,
    
    'magnitude': magnitude,
    'mag': magnitude,  # Alias
    'norm': magnitude,  # Alias
    'normalize': normalize,
    'unit': normalize,  # Alias
    
    'dot': dot,
    'cross': cross,
    'angle': angle_between,
    'angle_between': angle_between,
    'projection': projection,
    'proj': projection,  # Alias
    'distance': distance,
    'dist': distance,  # Alias
    
    'vadd': add_vectors,
    'vsub': subtract_vectors,
    'vscale': scalar_multiply,
}

def get_function(name):
    """Get a vector function by name"""
    if name in VECTOR_FUNCTIONS:
        return VECTOR_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown vector function: {name}")