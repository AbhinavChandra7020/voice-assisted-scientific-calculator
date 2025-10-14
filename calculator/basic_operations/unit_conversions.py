# length conversion
LENGTH_TO_METERS = {
    # metric
    'km': 1000,
    'meter': 1,
    'm': 1,
    'cm': 0.01,
    'mm': 0.001,
    'micrometer': 1e-6,
    'um': 1e-6,
    'nanometer': 1e-9,
    'nm': 1e-9,
    
    # imperial
    'mile': 1609.344,
    'mi': 1609.344,
    'yard': 0.9144,
    'yd': 0.9144,
    'foot': 0.3048,
    'ft': 0.3048,
    'inch': 0.0254,
    'in': 0.0254,
    
    # nautical
    'nautical_mile': 1852,
    'nmi': 1852,
}

def convert_length(value, from_unit, to_unit):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in LENGTH_TO_METERS:
        raise ValueError(f"Unknown length unit: {from_unit}")
    if to_unit not in LENGTH_TO_METERS:
        raise ValueError(f"Unknown length unit: {to_unit}")
    
    # Convert to meters, then to target unit
    meters = value * LENGTH_TO_METERS[from_unit]
    result = meters / LENGTH_TO_METERS[to_unit]
    return result


# mass conversion
MASS_TO_KG = {
    # metric
    'ton': 1000,
    'tonne': 1000,
    'kg': 1,
    'kilogram': 1,
    'gram': 0.001,
    'g': 0.001,
    'mg': 1e-6,
    'milligram': 1e-6,
    'microgram': 1e-9,
    'ug': 1e-9,
    
    # imperial
    'pound': 0.45359237,
    'lb': 0.45359237,
    'ounce': 0.028349523125,
    'oz': 0.028349523125,
    'stone': 6.35029318,
    'ton_us': 907.18474,
    'ton_uk': 1016.0469088,
}

def convert_mass(value, from_unit, to_unit):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in MASS_TO_KG:
        raise ValueError(f"Unknown mass unit: {from_unit}")
    if to_unit not in MASS_TO_KG:
        raise ValueError(f"Unknown mass unit: {to_unit}")
    
    kg = value * MASS_TO_KG[from_unit]
    result = kg / MASS_TO_KG[to_unit]
    return result


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature(value, from_unit, to_unit):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    unit_map = {'celsius': 'c', 'fahrenheit': 'f', 'kelvin': 'k'}
    from_unit = unit_map.get(from_unit, from_unit)
    to_unit = unit_map.get(to_unit, to_unit)
    
    if from_unit == to_unit:
        return value
    
    if from_unit == 'c':
        celsius = value
    elif from_unit == 'f':
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == 'k':
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Unknown temperature unit: {from_unit}")
    
    if to_unit == 'c':
        return celsius
    elif to_unit == 'f':
        return celsius_to_fahrenheit(celsius)
    elif to_unit == 'k':
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError(f"Unknown temperature unit: {to_unit}")


# time conversion
TIME_TO_SECONDS = {
    'week': 604800,
    'day': 86400,
    'hour': 3600,
    'hr': 3600,
    'h': 3600,
    'minute': 60,
    'min': 60,
    'second': 1,
    'sec': 1,
    's': 1,
    'millisecond': 0.001,
    'ms': 0.001,
    'microsecond': 1e-6,
    'us': 1e-6,
    'nanosecond': 1e-9,
    'ns': 1e-9,
}

def convert_time(value, from_unit, to_unit):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in TIME_TO_SECONDS:
        raise ValueError(f"Unknown time unit: {from_unit}")
    if to_unit not in TIME_TO_SECONDS:
        raise ValueError(f"Unknown time unit: {to_unit}")
    
    seconds = value * TIME_TO_SECONDS[from_unit]
    result = seconds / TIME_TO_SECONDS[to_unit]
    return result


# area conversion
AREA_TO_SQ_METERS = {
    'km2': 1e6,
    'sq_km': 1e6,
    'm2': 1,
    'sq_m': 1,
    'cm2': 1e-4,
    'sq_cm': 1e-4,
    'mm2': 1e-6,
    'sq_mm': 1e-6,
    'hectare': 10000,
    'ha': 10000,
    'acre': 4046.8564224,
    'sq_mile': 2589988.110336,
    'sq_mi': 2589988.110336,
    'sq_yard': 0.83612736,
    'sq_yd': 0.83612736,
    'sq_foot': 0.09290304,
    'sq_ft': 0.09290304,
    'sq_inch': 0.00064516,
    'sq_in': 0.00064516,
}

def convert_area(value, from_unit, to_unit):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in AREA_TO_SQ_METERS:
        raise ValueError(f"Unknown area unit: {from_unit}")
    if to_unit not in AREA_TO_SQ_METERS:
        raise ValueError(f"Unknown area unit: {to_unit}")
    
    sq_meters = value * AREA_TO_SQ_METERS[from_unit]
    result = sq_meters / AREA_TO_SQ_METERS[to_unit]
    return result


# volume conversion
VOLUME_TO_LITERS = {
    # metric
    'kiloliter': 1000,
    'kl': 1000,
    'liter': 1,
    'l': 1,
    'milliliter': 0.001,
    'ml': 0.001,
    'cubic_meter': 1000,
    'm3': 1000,
    'cubic_cm': 0.001,
    'cm3': 0.001,
    'cc': 0.001,
    
    'gallon': 3.785411784,
    'gal': 3.785411784,
    'quart': 0.946352946,
    'qt': 0.946352946,
    'pint': 0.473176473,
    'pt': 0.473176473,
    'cup': 0.2365882365,
    'fluid_ounce': 0.0295735295625,
    'fl_oz': 0.0295735295625,
    'tablespoon': 0.01478676478125,
    'tbsp': 0.01478676478125,
    'teaspoon': 0.00492892159375,
    'tsp': 0.00492892159375,
    
    'gallon_uk': 4.54609,
    'gal_uk': 4.54609,
}

def convert_volume(value, from_unit, to_unit):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in VOLUME_TO_LITERS:
        raise ValueError(f"Unknown volume unit: {from_unit}")
    if to_unit not in VOLUME_TO_LITERS:
        raise ValueError(f"Unknown volume unit: {to_unit}")
    
    liters = value * VOLUME_TO_LITERS[from_unit]
    result = liters / VOLUME_TO_LITERS[to_unit]
    return result


# speed conversion
SPEED_TO_MPS = {
    'mps': 1,
    'm/s': 1,
    'kph': 0.277778,
    'km/h': 0.277778,
    'kmh': 0.277778,
    'mph': 0.44704,
    'mi/h': 0.44704,
    'knot': 0.514444,
    'kt': 0.514444,
    'fps': 0.3048,
    'ft/s': 0.3048,
}

def convert_speed(value, from_unit, to_unit):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in SPEED_TO_MPS:
        raise ValueError(f"Unknown speed unit: {from_unit}")
    if to_unit not in SPEED_TO_MPS:
        raise ValueError(f"Unknown speed unit: {to_unit}")
    
    mps = value * SPEED_TO_MPS[from_unit]
    result = mps / SPEED_TO_MPS[to_unit]
    return result


# energy conversion
ENERGY_TO_JOULES = {
    'joule': 1,
    'j': 1,
    'kilojoule': 1000,
    'kj': 1000,
    'calorie': 4.184,
    'cal': 4.184,
    'kilocalorie': 4184,
    'kcal': 4184,
    'watt_hour': 3600,
    'wh': 3600,
    'kilowatt_hour': 3.6e6,
    'kwh': 3.6e6,
    'electronvolt': 1.602176634e-19,
    'ev': 1.602176634e-19,
    'btu': 1055.06,
}

def convert_energy(value, from_unit, to_unit):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in ENERGY_TO_JOULES:
        raise ValueError(f"Unknown energy unit: {from_unit}")
    if to_unit not in ENERGY_TO_JOULES:
        raise ValueError(f"Unknown energy unit: {to_unit}")
    
    joules = value * ENERGY_TO_JOULES[from_unit]
    result = joules / ENERGY_TO_JOULES[to_unit]
    return result


# pressure conversion
PRESSURE_TO_PASCAL = {
    'pascal': 1,
    'pa': 1,
    'kilopascal': 1000,
    'kpa': 1000,
    'bar': 100000,
    'atmosphere': 101325,
    'atm': 101325,
    'psi': 6894.757,
    'mmhg': 133.322,
    'torr': 133.322,
}

def convert_pressure(value, from_unit, to_unit):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in PRESSURE_TO_PASCAL:
        raise ValueError(f"Unknown pressure unit: {from_unit}")
    if to_unit not in PRESSURE_TO_PASCAL:
        raise ValueError(f"Unknown pressure unit: {to_unit}")
    
    pascal = value * PRESSURE_TO_PASCAL[from_unit]
    result = pascal / PRESSURE_TO_PASCAL[to_unit]
    return result


def dms_to_decimal(degrees, minutes=0, seconds=0):

    decimal = abs(degrees) + minutes/60 + seconds/3600
    if degrees < 0:
        decimal = -decimal
    return decimal

def decimal_to_dms(decimal_degrees):

    negative = decimal_degrees < 0
    decimal_degrees = abs(decimal_degrees)
    
    degrees = int(decimal_degrees)
    minutes_decimal = (decimal_degrees - degrees) * 60
    minutes = int(minutes_decimal)
    seconds = (minutes_decimal - minutes) * 60
    
    if negative:
        degrees = -degrees
    
    return (degrees, minutes, seconds)

def dms_add(d1, m1, s1, d2, m2, s2):

    dec1 = dms_to_decimal(d1, m1, s1)
    dec2 = dms_to_decimal(d2, m2, s2)
    result = dec1 + dec2
    return decimal_to_dms(result)

def dms_subtract(d1, m1, s1, d2, m2, s2):

    dec1 = dms_to_decimal(d1, m1, s1)
    dec2 = dms_to_decimal(d2, m2, s2)
    result = dec1 - dec2
    return decimal_to_dms(result)

def convert_angle(value, from_unit, to_unit):

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    # radian conversion
    if from_unit in ['deg', 'degree', 'degrees']:
        radians = value * (3.141592653589793 / 180)
    elif from_unit in ['rad', 'radian', 'radians']:
        radians = value
    elif from_unit in ['grad', 'gradian', 'gradians']:
        radians = value * (3.141592653589793 / 200)
    elif from_unit in ['turn', 'revolution']:
        radians = value * (2 * 3.141592653589793)
    else:
        raise ValueError(f"Unknown angle unit: {from_unit}")
    
    # radian to target
    if to_unit in ['deg', 'degree', 'degrees']:
        return radians * (180 / 3.141592653589793)
    elif to_unit in ['rad', 'radian', 'radians']:
        return radians
    elif to_unit in ['grad', 'gradian', 'gradians']:
        return radians * (200 / 3.141592653589793)
    elif to_unit in ['turn', 'revolution']:
        return radians / (2 * 3.141592653589793)
    else:
        raise ValueError(f"Unknown angle unit: {to_unit}")


UNIT_CONVERSION_FUNCTIONS = {
    # length
    'convert_length': convert_length,
    'conv_len': convert_length,
    
    # mass
    'convert_mass': convert_mass,
    'conv_mass': convert_mass,
    
    # temperature
    'convert_temp': convert_temperature,
    'conv_temp': convert_temperature,
    'c_to_f': celsius_to_fahrenheit,
    'f_to_c': fahrenheit_to_celsius,
    'c_to_k': celsius_to_kelvin,
    'k_to_c': kelvin_to_celsius,
    
    # time
    'convert_time': convert_time,
    'conv_time': convert_time,
    
    # area
    'convert_area': convert_area,
    'conv_area': convert_area,
    
    # volume
    'convert_volume': convert_volume,
    'conv_vol': convert_volume,
    
    # speed
    'convert_speed': convert_speed,
    'conv_speed': convert_speed,
    
    # energy
    'convert_energy': convert_energy,
    'conv_energy': convert_energy,
    
    # pressure
    'convert_pressure': convert_pressure,
    'conv_pressure': convert_pressure,

    'dms_to_dec': dms_to_decimal,
    'dec_to_dms': decimal_to_dms,
    'dms_add': dms_add,
    'dms_sub': dms_subtract,
    'convert_angle': convert_angle,
    'conv_angle': convert_angle,
}

def get_function(name):
    if name in UNIT_CONVERSION_FUNCTIONS:
        return UNIT_CONVERSION_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown unit conversion function: {name}")