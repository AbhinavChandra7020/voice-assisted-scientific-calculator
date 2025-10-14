
from fractions import Fraction as PyFraction

def fraction(numerator, denominator=1):

    return PyFraction(int(numerator), int(denominator))

def decimal_to_fraction(decimal_value, max_denominator=1000000):

    return PyFraction(decimal_value).limit_denominator(max_denominator)

def fraction_to_decimal(frac):

    if isinstance(frac, PyFraction):
        return float(frac)
    else:
        raise ValueError("Input must be a Fraction")

def mixed_number(whole, numerator, denominator):

    whole = int(whole)
    frac = PyFraction(int(numerator), int(denominator))
    if whole >= 0:
        return whole + frac
    else:
        return whole - frac

def to_mixed_number(frac):

    if not isinstance(frac, PyFraction):
        frac = PyFraction(frac).limit_denominator()
    
    whole = int(frac)
    remainder = frac - whole
    
    if remainder == 0:
        return (whole, 0, 1)
    else:
        return (whole, remainder.numerator, remainder.denominator)

def simplify_fraction(numerator, denominator):

    return PyFraction(int(numerator), int(denominator))

def frac_add(frac1, frac2):
    if not isinstance(frac1, PyFraction):
        frac1 = PyFraction(frac1).limit_denominator()
    if not isinstance(frac2, PyFraction):
        frac2 = PyFraction(frac2).limit_denominator()
    return frac1 + frac2

def frac_subtract(frac1, frac2):
    if not isinstance(frac1, PyFraction):
        frac1 = PyFraction(frac1).limit_denominator()
    if not isinstance(frac2, PyFraction):
        frac2 = PyFraction(frac2).limit_denominator()
    return frac1 - frac2

def frac_multiply(frac1, frac2):
    if not isinstance(frac1, PyFraction):
        frac1 = PyFraction(frac1).limit_denominator()
    if not isinstance(frac2, PyFraction):
        frac2 = PyFraction(frac2).limit_denominator()
    return frac1 * frac2

def frac_divide(frac1, frac2):
    if not isinstance(frac1, PyFraction):
        frac1 = PyFraction(frac1).limit_denominator()
    if not isinstance(frac2, PyFraction):
        frac2 = PyFraction(frac2).limit_denominator()
    return frac1 / frac2


FRACTION_FUNCTIONS = {
    'fraction': fraction,
    'frac': fraction,
    'dec_to_frac': decimal_to_fraction,
    'd2f': decimal_to_fraction,
    'frac_to_dec': fraction_to_decimal,
    'f2d': fraction_to_decimal,
    'mixed': mixed_number,
    'to_mixed': to_mixed_number,
    'simplify': simplify_fraction,
    'frac_add': frac_add,
    'frac_sub': frac_subtract,
    'frac_mul': frac_multiply,
    'frac_div': frac_divide,
}

def get_function(name):
    if name in FRACTION_FUNCTIONS:
        return FRACTION_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown fraction function: {name}")