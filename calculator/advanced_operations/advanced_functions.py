import math

# hyperbolic functions
def sinh(x):
    return math.sinh(x)

def cosh(x):
    return math.cosh(x)

def tanh(x):
    return math.tanh(x)

def asinh(x):
    return math.asinh(x)

def acosh(x):
    return math.acosh(x)

def atanh(x):
    return math.atanh(x)

# combination
def nCr(n, r):
    return math.comb(int(n), int(r))

# permutation
def nPr(n, r):
    return math.perm(int(n), int(r))

# Additional mathematical functions
def gcd(a, b):
    return math.gcd(int(a), int(b))

def lcm(a, b):
    return math.lcm(int(a), int(b))

def deg_to_rad(degrees):
    return math.radians(degrees)

def rad_to_deg(radians):
    return math.degrees(radians)

def prime_factorization(n):

    n = int(n)
    if n < 2:
        return []
    
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    
    if n > 1:
        factors.append(n)
    
    return factors

def is_prime(n):

    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True

def rectangular_to_polar(x, y):

    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return (r, theta)

def polar_to_rectangular(r, theta):

    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

def spherical_to_cartesian(r, theta, phi):

    x = r * math.sin(phi) * math.cos(theta)
    y = r * math.sin(phi) * math.sin(theta)
    z = r * math.cos(phi)
    return (x, y, z)

def cartesian_to_spherical(x, y, z):

    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / r) if r != 0 else 0
    return (r, theta, phi)

ADVANCED_FUNCTIONS = {
    # hyperbolic
    'sinh': sinh,
    'cosh': cosh,
    'tanh': tanh,
    'asinh': asinh,
    'acosh': acosh,
    'atanh': atanh,
    
    # combinatorics
    'nCr': nCr,
    'nPr': nPr,
    'comb': nCr,  
    'perm': nPr,  
    
    # utility
    'gcd': gcd,
    'lcm': lcm,
    'deg': deg_to_rad, 
    'rad': rad_to_deg,

    # prime numbers
    'prime_factors': prime_factorization,
    'factorize': prime_factorization,  
    'is_prime': is_prime,  

    # coordinate conversions
    'rect_to_polar': rectangular_to_polar,
    'polar_to_rect': polar_to_rectangular,
    'r2p': rectangular_to_polar,  
    'p2r': polar_to_rectangular, 
    'sph_to_cart': spherical_to_cartesian,
    'cart_to_sph': cartesian_to_spherical,
}

def get_function(name):
    if name in ADVANCED_FUNCTIONS:
        return ADVANCED_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown advanced function: {name}")