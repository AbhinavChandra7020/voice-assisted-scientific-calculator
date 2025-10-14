# conversion functions

def decimal_to_binary(n):

    n = int(n)
    return bin(n)

def decimal_to_octal(n):

    n = int(n)
    return oct(n)

def decimal_to_hex(n):

    n = int(n)
    return hex(n)

def binary_to_decimal(binary_str):

    if isinstance(binary_str, str):
        if binary_str.startswith('0b') or binary_str.startswith('0B'):
            binary_str = binary_str[2:]
        return int(binary_str, 2)
    else:
        raise ValueError("Binary input must be a string")

def octal_to_decimal(octal_str):

    if isinstance(octal_str, str):
        if octal_str.startswith('0o') or octal_str.startswith('0O'):
            octal_str = octal_str[2:]
        return int(octal_str, 8)
    else:
        raise ValueError("Octal input must be a string")

def hex_to_decimal(hex_str):

    if isinstance(hex_str, str):
        if hex_str.startswith('0x') or hex_str.startswith('0X'):
            hex_str = hex_str[2:]
        return int(hex_str, 16)
    else:
        raise ValueError("Hexadecimal input must be a string")

def to_base(n, base):

    n = int(n)
    base = int(base)
    
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    
    if n == 0:
        return '0'
    
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    negative = n < 0
    n = abs(n)
    
    while n > 0:
        result.append(digits[n % base])
        n //= base
    
    if negative:
        result.append('-')
    
    return ''.join(reversed(result))

def from_base(value_str, base):

    base = int(base)
    
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    
    if not isinstance(value_str, str):
        raise ValueError("Value must be a string")
    
    return int(value_str, base)

# bitwise operations
def bitwise_and(a, b):

    return int(a) & int(b)

def bitwise_or(a, b):

    return int(a) | int(b)

def bitwise_xor(a, b):

    return int(a) ^ int(b)

def bitwise_not(a):

    return ~int(a)

def left_shift(a, n):

    return int(a) << int(n)

def right_shift(a, n):

    return int(a) >> int(n)


BASE_CONVERSION_FUNCTIONS = {
    # decimal to other bases
    'bin': decimal_to_binary,
    'oct': decimal_to_octal,
    'hex': decimal_to_hex,
    
    # other bases to decimal
    'bin_to_dec': binary_to_decimal,
    'oct_to_dec': octal_to_decimal,
    'hex_to_dec': hex_to_decimal,
    
    # general base conversion
    'to_base': to_base,
    'from_base': from_base,
    
    # bitwise operations
    'bit_and': bitwise_and,
    'bit_or': bitwise_or,
    'bit_xor': bitwise_xor,
    'bit_not': bitwise_not,
    'lshift': left_shift,
    'rshift': right_shift,
}

def get_function(name):
    if name in BASE_CONVERSION_FUNCTIONS:
        return BASE_CONVERSION_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown base conversion function: {name}")