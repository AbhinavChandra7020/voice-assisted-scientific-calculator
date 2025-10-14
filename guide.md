# Scientific Calculator CLI - User Guide

## Table of Contents
- [Getting Started](#getting-started)
- [Basic Calculations](#basic-calculations)
- [Scientific Functions](#scientific-functions)
- [Advanced Operations](#advanced-operations)
- [Statistics](#statistics)
- [Unit Conversions](#unit-conversions)
- [Special Features](#special-features)
- [Tips & Tricks](#tips--tricks)

---

## Getting Started

### Starting the Calculator
```bash
python main.py
```

### Basic Commands
- Type any mathematical expression and press Enter
- Type `quit` or `exit` to close
- Type `mode` to see current angle mode
- Type `deg` or `rad` to switch angle modes

### Angle Modes
The calculator supports two angle modes for trigonometric functions:
- **DEG** (Degrees) - Default mode
- **RAD** (Radians)

```
>>> mode
Current mode: DEG

>>> deg
Mode set to: DEGREES

>>> rad
Mode set to: RADIANS
```

---

## Basic Calculations

### Arithmetic Operations
```
>>> 5 + 3
= 8

>>> 10 - 4
= 6

>>> 7 * 8
= 56

>>> 20 / 4
= 5.0

>>> 2 ** 8
= 256

>>> 17 % 5
= 2
```

### Using ANS (Previous Answer)
```
>>> 5 + 5
= 10

>>> ans * 2
= 20

>>> ans + 100
= 120
```

### Order of Operations
```
>>> 2 + 3 * 4
= 14

>>> (2 + 3) * 4
= 20
```

### Multi-Statement Commands
Execute multiple calculations at once with `:` separator:
```
>>> 5+5 : ans*2 : ans-5
= [10, 20, 15]
```

---

## Scientific Functions

### Basic Functions
```
>>> abs(-5)
= 5

>>> sqrt(16)
= 4.0

>>> cbrt(27)
= 3.0

>>> nthroot(32, 5)
= 2.0

>>> factorial(5)
= 120
```

### Trigonometric Functions
Make sure you're in the correct angle mode!

**Degrees mode:**
```
>>> deg
>>> sin(30)
= 0.5

>>> cos(60)
= 0.5

>>> tan(45)
= 1.0
```

**Radians mode:**
```
>>> rad
>>> sin(pi/2)
= 1.0

>>> cos(0)
= 1.0
```

### Inverse Trigonometric
```
>>> asin(0.5)
= 30.0  (in DEG mode)

>>> acos(0.5)
= 60.0  (in DEG mode)

>>> atan(1)
= 45.0  (in DEG mode)
```

### Hyperbolic Functions
```
>>> sinh(1)
= 1.1752011936438014

>>> cosh(0)
= 1.0

>>> tanh(1)
= 0.7615941559557649
```

### Logarithmic Functions
```
>>> log(100)
= 2.0  (log base 10)

>>> ln(e)
= 1.0  (natural log)

>>> log2(8)
= 3.0  (log base 2)

>>> exp(1)
= 2.718281828459045
```

### Constants
```
>>> pi
= 3.141592653589793

>>> e
= 2.718281828459045

>>> phi
= 1.618033988749895  (golden ratio)

>>> const('c')
= 299792458  (speed of light)
```

---

## Advanced Operations

### Complex Numbers
```
>>> 3 + 4*j
= (3+4j)

>>> abs(3 + 4*j)
= 5.0

>>> conj(3 + 4*j)
= (3-4j)

>>> csqrt(-1)
= 1j
```

### Matrices
```
>>> [[1,2],[3,4]]
= [[1, 2], [3, 4]]

>>> [[1,2],[3,4]] + [[5,6],[7,8]]
= [[6, 8], [10, 12]]

>>> [[1,2],[3,4]] * [[5,6],[7,8]]
= [[19, 22], [43, 50]]

>>> det([[1,2],[3,4]])
= -2.0

>>> transpose([[1,2,3],[4,5,6]])
= [[1, 4], [2, 5], [3, 6]]

>>> inv([[1,2],[3,4]])
= [[-2.0, 1.0], [1.5, -0.5]]
```

### Vectors
```
>>> magnitude([3, 4])
= 5.0

>>> dot([1, 2, 3], [4, 5, 6])
= 32

>>> cross([1, 0, 0], [0, 1, 0])
= [0, 0, 1]

>>> normalize([3, 4])
= [0.6, 0.8]

>>> distance([0, 0], [3, 4])
= 5.0
```

### Calculus
```
>>> derivative("x**2", 3)
= 6.0

>>> derivative("sin(x)", 0)
= 1.0

>>> integrate("x**2", 0, 2)
= 2.666666666666667

>>> summation("i", 1, 10)
= 55

>>> summation("i**2", 1, 10)
= 385
```

### Equation Solving
```
>>> solve("x**2 - 5*x + 6")
= [2.0, 3.0]

>>> solve("x**2 - 4")
= [-2.0, 2.0]

>>> solve_inequality("x > 5")
= (5, oo)

>>> solve_inequality("2*x + 3 < 10")
= (-oo, 3.5)
```

---

## Statistics

### Basic Statistics
```
>>> mean([1, 2, 3, 4, 5])
= 3.0

>>> median([1, 2, 3, 4, 5])
= 3

>>> mode([1, 2, 2, 3, 3, 3])
= 3

>>> stdev([1, 2, 3, 4, 5])
= 1.5811388300841898

>>> variance([1, 2, 3, 4, 5])
= 2.5
```

### Advanced Statistics
```
>>> correlation([1, 2, 3], [2, 4, 6])
= 1.0

>>> linreg([1, 2, 3], [2, 4, 6])
= (2.0, 0.0)

>>> quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9])
= [2.5, 5.0, 7.5]

>>> zscore([1, 2, 3, 4, 5], 5)
= 1.414213562373095
```

### Probability Distributions
```
>>> norm_cdf(0, 0, 1)
= 0.5

>>> norm_inv(0.95, 0, 1)
= 1.6448536269514722

>>> binom_pmf(5, 10, 0.5)
= 0.24609375
```

---

## Unit Conversions

### Length
```
>>> convert_length(1, 'km', 'm')
= 1000.0

>>> convert_length(1, 'mile', 'km')
= 1.609344
```

### Mass
```
>>> convert_mass(1, 'kg', 'lb')
= 2.20462262185

>>> convert_mass(100, 'lb', 'kg')
= 45.359237
```

### Temperature
```
>>> c_to_f(0)
= 32.0

>>> c_to_f(100)
= 212.0

>>> f_to_c(32)
= 0.0

>>> convert_temp(100, 'c', 'k')
= 373.15
```

### Time
```
>>> convert_time(1, 'hour', 'minute')
= 60.0

>>> convert_time(1, 'day', 'hour')
= 24.0
```

### Speed
```
>>> convert_speed(100, 'kph', 'mph')
= 62.13711922373339
```

### Volume
```
>>> convert_volume(1, 'gallon', 'liter')
= 3.785411784
```

### Angles (DMS)
```
>>> dms_to_dec(45, 30, 0)
= 45.5

>>> dec_to_dms(45.5)
= (45, 30, 0.0)

>>> convert_angle(180, 'deg', 'rad')
= 3.141592653589793
```

---

## Special Features

### Fractions
```
>>> fraction(3, 4)
= Fraction(3, 4)

>>> dec_to_frac(0.75)
= Fraction(3, 4)

>>> dec_to_frac(0.333333)
= Fraction(1, 3)

>>> to_mixed(fraction(7, 3))
= (2, 1, 3)
```

### Ratios
```
>>> ratio(6, 8)
= (3, 4)

>>> proportion(2, 3, 4, 'd')
= 6.0

>>> split_ratio(100, 2, 3)
= [40.0, 60.0]

>>> aspect_ratio(1920, 1080)
= (16, 9)
```

### Base Conversions
```
>>> bin(10)
= '0b1010'

>>> hex(255)
= '0xff'

>>> hex_to_dec('ff')
= 255

>>> to_base(255, 2)
= '11111111'
```

### Logical Operations
```
>>> AND(1, 1)
= 1

>>> OR(1, 0)
= 1

>>> NOT(1)
= 0

>>> XOR(1, 1)
= 0

>>> NAND(1, 1)
= 0
```

### Random Numbers
```
>>> rand()
= 0.7234567...

>>> randint(1, 10)
= 7

>>> choice([1, 2, 3, 4, 5])
= 3
```

### Prime Numbers
```
>>> prime_factors(60)
= [2, 2, 3, 5]

>>> is_prime(17)
= True

>>> is_prime(18)
= False
```

### Combinatorics
```
>>> nCr(5, 2)
= 10

>>> nPr(5, 2)
= 20

>>> factorial(5)
= 120
```

### Coordinate Conversions
```
>>> rect_to_polar(3, 4)
= (5.0, 0.9272952180016122)

>>> polar_to_rect(5, 0.927)
= (3.001180741..., 3.999114171...)
```

---

## Tips & Tricks

### 1. Use Parentheses for Clarity
```
>>> 2 + 3 * 4
= 14

>>> (2 + 3) * 4
= 20
```

### 2. Chain Calculations with ANS
```
>>> 100
= 100

>>> ans / 2
= 50.0

>>> ans + 25
= 75.0
```

### 3. Work with Lists for Data Analysis
```
>>> data = [1, 2, 3, 4, 5]
>>> mean(data)
= 3.0

>>> stdev(data)
= 1.58...
```

### 4. Switch Angle Modes as Needed
```
>>> deg
>>> sin(90)
= 1.0

>>> rad
>>> sin(pi/2)
= 1.0
```

### 5. Use Multi-Statement for Workflows
```
>>> 100 : ans*0.2 : ans+50
= [100, 20.0, 70.0]
```

### 6. Combine Functions
```
>>> sqrt(abs(-16))
= 4.0

>>> sin(asin(0.5))
= 0.5

>>> magnitude(cross([1,0,0], [0,1,0]))
= 1.0
```

### 7. View Calculation History
```
>>> history(5)
Shows last 5 calculations
```

---

## Common Function Reference

### Mathematical Functions
| Function | Description | Example |
|----------|-------------|---------|
| `abs(x)` | Absolute value | `abs(-5)` → 5 |
| `sqrt(x)` | Square root | `sqrt(16)` → 4.0 |
| `cbrt(x)` | Cube root | `cbrt(27)` → 3.0 |
| `sin(x)` | Sine | `sin(30)` → 0.5 |
| `cos(x)` | Cosine | `cos(60)` → 0.5 |
| `tan(x)` | Tangent | `tan(45)` → 1.0 |
| `log(x)` | Log base 10 | `log(100)` → 2.0 |
| `ln(x)` | Natural log | `ln(e)` → 1.0 |
| `exp(x)` | e^x | `exp(1)` → 2.718... |

### Statistical Functions
| Function | Description | Example |
|----------|-------------|---------|
| `mean(list)` | Average | `mean([1,2,3])` → 2.0 |
| `median(list)` | Middle value | `median([1,2,3])` → 2 |
| `stdev(list)` | Std deviation | `stdev([1,2,3,4,5])` → 1.58 |
| `correlation(x,y)` | Correlation | `correlation([1,2,3],[2,4,6])` → 1.0 |

### Conversion Functions
| Function | Description | Example |
|----------|-------------|---------|
| `convert_length(v,from,to)` | Length | `convert_length(1,'km','m')` → 1000 |
| `convert_mass(v,from,to)` | Mass | `convert_mass(1,'kg','lb')` → 2.2 |
| `convert_temp(v,from,to)` | Temperature | `convert_temp(0,'c','f')` → 32 |
| `c_to_f(x)` | Celsius to F | `c_to_f(0)` → 32.0 |

---
