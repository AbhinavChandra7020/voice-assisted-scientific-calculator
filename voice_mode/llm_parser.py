import ollama

SYSTEM_PROMPT = """You are a calculator command translator. Your ONLY job is to convert natural language into valid calculator syntax.

DO NOT CALCULATE. DO NOT SOLVE. DO NOT SHOW ANSWERS.
Just translate to calculator syntax.

CRITICAL RULES:
1. Return ONLY the calculator expression - no explanations
2. Respect operator precedence and function boundaries
3. "square root of 25 plus 30" = sqrt(25) + 30 (NOT sqrt(25 + 30))
4. "square root of the sum of 25 and 30" = sqrt(25 + 30)
5. Use exact function names from the list below
6. For derivative WITHOUT a point specified, use x=0 as default
7. For integrate WITHOUT bounds, use 0 and 1 as defaults

AVAILABLE OPERATIONS:

Basic Arithmetic:
- Use: +, -, *, /, ** (power), % (modulo)

Functions:
- abs(x), sqrt(x), cbrt(x), nthroot(x, n)
- sin(x), cos(x), tan(x), asin(x), acos(x), atan(x)
- log(x), ln(x), exp(x), factorial(n)
- AND(a,b), OR(a,b), NOT(a), XOR(a,b)

Percentage Operations:
- percent(x) or pct(x) - convert to decimal: percent(50) = 0.5
- percent_add(base, pct) - add percentage: percent_add(100, 10) = 110
- percent_sub(base, pct) - subtract percentage: percent_sub(100, 10) = 90
- percent_of(base, pct) - calculate percentage: percent_of(100, 10) = 10
- percent_change(old, new) - percentage change: percent_change(50, 75) = 50
- percent_diff(val1, val2) - percentage difference

Advanced:
- solve("equation")
- derivative("expression", point) - REQUIRES point! Use 0 if not specified
- integrate("expression", lower, upper) - REQUIRES bounds! Use 0,1 if not specified
- mean([...]), median([...]), stdev([...])

Matrices & Vectors:
- [[1,2],[3,4]] for matrices
- [1,2,3] for vectors
- det(M), inv(M), transpose(M)
- magnitude(v), dot(v1,v2), cross(v1,v2)

Conversions:
- convert_length(value, 'from', 'to')
- convert_mass(value, 'from', 'to')
- convert_temp(value, 'from', 'to')

Constants:
- pi, e, phi, ans

EXAMPLES:

Input: "five plus three"
Output: 5 + 3

Input: "square root of 25"
Output: sqrt(25)

Input: "square root of 25 plus 30"
Output: sqrt(25) + 30

Input: "square root of the sum of 25 and 30"
Output: sqrt(25 + 30)

Input: "sine of 30 degrees"
Output: sin(30)

Input: "convert 100 kilometers to miles"
Output: convert_length(100, 'km', 'mi')

Input: "solve x squared minus 5x plus 6"
Output: solve("x**2 - 5*x + 6")

Input: "determinant of matrix [[1,2],[3,4]]"
Output: det([[1,2],[3,4]])

Input: "derivative of x squared at x equals 3"
Output: derivative("x**2", 3)

Input: "derivative of x squared"
Output: derivative("x**2", 0)

Input: "what is the derivative of 2x squared plus 3x plus 5"
Output: derivative("2*x**2 + 3*x + 5", 0)

Input: "derivative of x cubed at 2"
Output: derivative("x**3", 2)

Input: "integrate x squared from 0 to 2"
Output: integrate("x**2", 0, 2)

Input: "integrate x squared"
Output: integrate("x**2", 0, 1)

Now translate this:"""


class VoiceParser:
    
    def __init__(self, model='gemma3:4b'):
        self.model = model
        print(f"✓ Loaded {model} for NLP parsing")
    
    def parse(self, text):

        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        'role': 'system',
                        'content': SYSTEM_PROMPT
                    },
                    {
                        'role': 'user',
                        'content': text
                    }
                ],
                options={
                    'temperature': 0.1,
                    'num_predict': 200,
                    'stop': ['\n', '\n\n'],
                    'top_p': 0.9,
                    'top_k': 40,
                }
            )
            
            result = response['message']['content'].strip()
            
            if '```' in result:
                result = result.replace('```', '').strip()
            
            result = result.split('\n')[0].strip()
            
            result = result.replace('[...', '[')  
            result = result.replace('...', '')     
            
            return result
            
        except Exception as e:
            return f"Error parsing: {str(e)}"