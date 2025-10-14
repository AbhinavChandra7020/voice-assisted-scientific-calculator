from fractions import Fraction
import math

def ratio(a, b):

    gcd = math.gcd(int(a), int(b))
    return (int(a // gcd), int(b // gcd))

def ratio_to_fraction(a, b):

    return Fraction(int(a), int(b))

def ratio_multiply(a, b, multiplier):

    return (a * multiplier, b * multiplier)

def ratio_divide(a, b, divisor):

    return ratio(a / divisor, b / divisor)

def proportion_solve(a, b, c, x_pos='d'):

    if x_pos == 'd':
        return (b * c) / a
    elif x_pos == 'c':
        return (a * c) / b
    else:
        raise ValueError("x_pos must be 'c' or 'd'")

def ratio_add(a1, b1, a2, b2):

    return (a1 + a2, b1 + b2)

def ratio_equal(a1, b1, a2, b2):

    return abs(a1 * b2 - a2 * b1) < 1e-10

def split_by_ratio(total, *parts):

    total_parts = sum(parts)
    return [total * (part / total_parts) for part in parts]

def aspect_ratio(width, height):

    return ratio(width, height)


RATIO_FUNCTIONS = {
    'ratio': ratio,
    'ratio_to_frac': ratio_to_fraction,
    'ratio_mul': ratio_multiply,
    'ratio_div': ratio_divide,
    'proportion': proportion_solve,
    'ratio_add': ratio_add,
    'ratio_equal': ratio_equal,
    'split_ratio': split_by_ratio,
    'aspect_ratio': aspect_ratio,
}

def get_function(name):
    """Get a ratio function by name"""
    if name in RATIO_FUNCTIONS:
        return RATIO_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown ratio function: {name}")