# calculator/basic_operations/percent_operations.py

def percent_add(base, percent):
 
    return base * (1 + percent/100)

def percent_subtract(base, percent):

    return base * (1 - percent/100)

def percent_of(base, percent):

    return base * (percent/100)

def percent_change(old_value, new_value):

    return ((new_value - old_value) / old_value) * 100

def percent_difference(value1, value2):
 
    avg = (value1 + value2) / 2
    return abs(value1 - value2) / avg * 100

PERCENT_FUNCTIONS = {
    'percent': lambda x: x/100,
    'pct': lambda x: x/100,
    'percent_add': percent_add,
    'pct_add': percent_add,
    'percent_sub': percent_subtract,
    'pct_sub': percent_subtract,
    'percent_of': percent_of,
    'pct_of': percent_of,
    'percent_change': percent_change,
    'pct_change': percent_change,
    'percent_diff': percent_difference,
}

def get_function(name):
    if name in PERCENT_FUNCTIONS:
        return PERCENT_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown percent function: {name}")