# Casio fx-991EX Voice Calculator

> A modern, AI-powered scientific calculator inspired by the legendary Casio fx-991EX ClassWiz - my trusty calculator through countless calculations.
---
## Installation

### Prerequisites
```bash
Python 3.8 or higher
```

### Clone Repository
```bash
git clone https://github.com/yourusername/casio-calculator.git
cd casio-calculator
```

### Create Virtual Environment

**It's highly recommended to use a virtual environment to avoid dependency conflicts:**

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt, indicating the virtual environment is active.

### Install Dependencies

**All dependencies are listed in `requirements.txt`:**
```bash
pip install -r requirements.txt
```

**For voice support, also install:**
```bash
# Install Ollama from: https://ollama.com
# Then pull the model:
ollama pull gemma3:4b
```

### Optional: Setup Voice Mode

**If you want voice input functionality:**

1. **Whisper model** (auto-downloads on first use)
   - Sizes available: tiny, base, small, medium, large
   - Base model recommended (~140MB)

2. **Ollama + LLM Model:**
```bash
   # Download Ollama from: https://ollama.com
   # Install and run:
   ollama pull gemma3:4b
```

---

## Usage

### Activate Virtual Environment

**Before running the calculator, always activate your virtual environment:**

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### Launch GUI
```bash
python main_gui.py
```

### Launch CLI
```bash
python main.py
```

### Deactivate Virtual Environment

**When you're done, deactivate the virtual environment:**
```bash
deactivate
```

---

## Features

### Core Capabilities
- **552+ Mathematical Functions** - From basic arithmetic to advanced calculus
- **AI Voice Input** - Speak your calculations naturally using Whisper + LLM
- **Beautiful Math Notation** - See √, ∫, π, ², ³ in real-time
- **Smart Expression Parsing** - Auto-fixes implicit multiplication (5x → 5*x)
- **Editable Display** - Click, edit, and navigate with cursor control

### Mathematical Operations
- Basic arithmetic (+, -, ×, ÷, ^, %)
- Trigonometric functions (sin, cos, tan, asin, acos, atan)
- Hyperbolic functions (sinh, cosh, tanh)
- Logarithms (log, ln, log2)
- Calculus (derivatives, integrals, summations)
- Linear algebra (matrices, vectors, determinants)
- Statistics (mean, median, stdev, correlation)
- Probability distributions (normal, binomial, t, chi-square)
- Complex numbers
- Equation solving
- Inequality solving

### Advanced Features
- **Percentage Operations** - Add/subtract percentages, calculate changes
- **Unit Conversions** - Length, mass, temperature, time, speed, energy, pressure
- **Base Conversions** - Binary, octal, hexadecimal, custom bases
- **Fractions & Ratios** - Simplify, convert, and calculate
- **Prime Numbers** - Factorization, primality testing
- **Combinatorics** - Permutations, combinations, factorials
- **Coordinate Systems** - Rectangular ↔ Polar conversions
- **Physical Constants** - Speed of light, Planck constant, gravity, etc.

### User Experience
- **Modern GUI** - Rounded borders, gradient effects, hover animations
- **Keyboard Support** - Type naturally, use shortcuts
- **History Navigation** - Up/Down arrows to recall previous calculations
- **Multiple Themes** - Dark mode with purple accents
- **Responsive Design** - Tabbed function panels, collapsible history
- **Real-time Formatting** - See mathematical notation as you type

---

## Voice Input Guide

### How to Use Voice Mode

1. **Click the VOICE INPUT button**
2. **Speak your calculation clearly:**
   - "What is 10 percent of 500"
   - "Add 15 percent to 200"
   - "Solve x squared minus 5x plus 6"
   - "Derivative of x squared at 3"
   - "Integrate x squared from 0 to 2"
3. **Wait for transcription** (Whisper converts speech to text)
4. **Wait for parsing** (LLM converts to calculator syntax)
5. **Auto-calculate**

### Voice Examples
```
"Square root of 25"          → sqrt(25) → 5.0
"Sine of 30 degrees"         → sin(30) → 0.5
"10 percent of 500"          → percent_of(500, 10) → 50
"Determinant of [[1,2],[3,4]]" → det([[1,2],[3,4]]) → -2.0
"Mean of 1, 2, 3, 4, 5"      → mean([1,2,3,4,5]) → 3.0
```

---

## Quick Start Guide

### Basic Calculations
```python
# Arithmetic
5 + 3        # 8
10 * 2       # 20
2 ** 8       # 256

# Functions
sqrt(16)     # 4.0
sin(30)      # 0.5 (in DEG mode)
log(100)     # 2.0
factorial(5) # 120
```

### Percentage Operations
```python
percent(50)              # 0.5 (convert to decimal)
percent_add(100, 10)     # 110 (add 10% to 100)
percent_sub(100, 10)     # 90 (subtract 10%)
percent_of(100, 10)      # 10 (10% of 100)
percent_change(50, 75)   # 50 (50% increase)
```

### Matrices & Vectors
```python
# Matrices
det([[1,2],[3,4]])                    # -2.0
inv([[1,2],[3,4]])                    # Inverse matrix
transpose([[1,2,3],[4,5,6]])          # Transpose

# Vectors
magnitude([3, 4])                     # 5.0
dot([1,2,3], [4,5,6])                 # 32
cross([1,0,0], [0,1,0])               # [0, 0, 1]
```

### Calculus
```python
derivative("x**2", 3)                 # 6.0
integrate("x**2", 0, 2)               # 2.666...
summation("i**2", 1, 10)              # 385
solve("x**2 - 5*x + 6")               # [2.0, 3.0]
```

### Statistics
```python
mean([1,2,3,4,5])                     # 3.0
stdev([1,2,3,4,5])                    # 1.581...
correlation([1,2,3], [2,4,6])         # 1.0
norm_cdf(0, 0, 1)                     # 0.5
```

### Unit Conversions
```python
convert_length(100, 'km', 'mi')       # 62.137...
convert_temp(100, 'c', 'f')           # 212.0
c_to_f(37)                            # 98.6
convert_mass(1, 'kg', 'lb')           # 2.204...
```

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Calculate (=) |
| `Escape` | Clear (AC) |
| `Backspace` | Delete character |
| `Up Arrow` | Previous calculation |
| `Down Arrow` | Next calculation |
| `Ctrl+C` | Copy result |

---

## GUI Components

### Display Panel
- **Top**: Mathematical notation (√, ∫, π, ²)
- **Middle**: Editable expression with cursor
- **Bottom**: Large result display

### Function Tabs
- **Basic**: Trigonometry, logarithms, roots
- **Advanced**: Calculus, combinatorics, conversions
- **Statistics**: Mean, stdev, distributions
- **Matrix**: Linear algebra operations

### Number Pad
- Standard 0-9 digits
- Operators: +, -, ×, ÷
- Special: %, (, ), ans, =
- Actions: DEL, AC

---

## Project Structure
```
casio-calculator/
├── main.py                      # Entry point
├── requirements.txt             # Python dependencies
├── venv/                        # Virtual environment (created by you)
├── calculator/                  # Core calculation engine
│   ├── __init__.py
│   ├── parser.py               # Expression parser
│   ├── basic_operations/       # Basic math functions
│   ├── advanced_operations/    # Matrices, vectors, calculus
│   ├── constants/              # Mathematical & physical constants
│   └── utils/                  # Angle modes, history
├── gui/                        # Modern GUI (refactored)
│   ├── __init__.py
│   ├── main_window.py          # Main calculator window
│   ├── math_formatter.py       # Mathematical notation formatter
│   ├── menu_bar.py             # Menu creation
│   ├── display_panel.py        # Display widgets
│   ├── function_tabs.py        # Tabbed function buttons
│   ├── number_pad.py           # Number pad
│   ├── voice_handler.py        # Voice input logic
│   ├── calculation_engine.py   # Calculation processing
│   └── ui_helpers.py           # Dialogs (Quick Guide, About)
├── voice_mode/                 # AI voice input (optional)
│   ├── __init__.py
│   ├── audio_recorder.py       # Audio recording
│   ├── speech_to_text.py       # Whisper integration
│   └── llm_parser.py           # Natural language → calculator syntax
├── guide.md                    # Comprehensive user guide
└── README.md                   # This file
```

---

## Dependencies

All required packages are listed in `requirements.txt`. Key dependencies include:

- **numpy** - Numerical computations
- **scipy** - Scientific computing
- **sympy** - Symbolic mathematics
- **sounddevice** - Audio recording (optional, for voice)
- **soundfile** - Audio file handling (optional, for voice)
- **openai-whisper** - Speech recognition (optional, for voice)
- **ollama** - LLM integration (optional, for voice)

---
