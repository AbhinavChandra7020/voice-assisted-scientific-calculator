
# physics constants
PHYSICS_CONSTANTS = {
    # Fundamental constants
    'c': 299792458,              # Speed of light in vacuum (m/s)
    'h': 6.62607015e-34,         # Planck constant (J⋅s)
    'hbar': 1.054571817e-34,     # Reduced Planck constant (J⋅s)
    'G': 6.67430e-11,            # Gravitational constant (m³/kg⋅s²)
    'g': 9.80665,                # Standard gravity (m/s²)
    'e_charge': 1.602176634e-19, # Elementary charge (C)
    'me': 9.1093837015e-31,      # Electron mass (kg)
    'mp': 1.67262192369e-27,     # Proton mass (kg)
    'mn': 1.67492749804e-27,     # Neutron mass (kg)
    'Na': 6.02214076e23,         # Avogadro's number (mol⁻¹)
    'k': 1.380649e-23,           # Boltzmann constant (J/K)
    'R': 8.314462618,            # Gas constant (J/mol⋅K)
    'sigma': 5.670374419e-8,     # Stefan-Boltzmann constant (W/m²⋅K⁴)
    'epsilon0': 8.8541878128e-12,# Permittivity of free space (F/m)
    'mu0': 1.25663706212e-6,     # Permeability of free space (H/m)
    'alpha': 7.2973525693e-3,    # Fine structure constant
}

# chemistry constants
CHEMISTRY_CONSTANTS = {
    'u': 1.66053906660e-27,      # Atomic mass unit (kg)
    'F': 96485.33212,            # Faraday constant (C/mol)
    'Vm': 0.02241396954,         # Molar volume of ideal gas at STP (m³/mol)
}

# astronomy constants
ASTRONOMY_CONSTANTS = {
    'AU': 1.495978707e11,        # Astronomical unit (m)
    'ly': 9.4607304725808e15,    # Light year (m)
    'pc': 3.0856775814913673e16, # Parsec (m)
    'solar_mass': 1.98847e30,    # Solar mass (kg)
    'earth_mass': 5.97217e24,    # Earth mass (kg)
    'earth_radius': 6.371e6,     # Earth radius (m)
}

ALL_CONSTANTS = {
    **PHYSICS_CONSTANTS,
    **CHEMISTRY_CONSTANTS,
    **ASTRONOMY_CONSTANTS,
}

def get_constant(name):
    """Get a physical constant by name"""
    if name in ALL_CONSTANTS:
        return ALL_CONSTANTS[name]
    else:
        raise ValueError(f"Unknown physical constant: {name}")

def list_constants():
    return list(ALL_CONSTANTS.keys())

CONSTANT_FUNCTIONS = {
    'const': get_constant,
    'constant': get_constant,
    'list_constants': list_constants,
}

def get_function(name):
    """Get a constant function by name"""
    if name in CONSTANT_FUNCTIONS:
        return CONSTANT_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown constant function: {name}")