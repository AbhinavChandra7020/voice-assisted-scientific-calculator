import re
from calculator import calculate


class CalculationEngine:
    
    # implicit multiplication fixing
    KNOWN_FUNCTIONS = [
        'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh',
        'log', 'ln', 'log2', 'exp', 'sqrt', 'cbrt', 'abs', 'factorial', 
        'floor', 'ceil', 'round', 'nthroot', 'root',
        'derivative', 'diff', 'integrate', 'integral', 'summation', 'sigma', 'product',
        'solve', 'roots', 'solve_inequality',
        'det', 'transpose', 'inv', 'trace', 'rank', 'eigenvalues',
        'magnitude', 'dot', 'cross', 'normalize', 'distance',
        'mean', 'median', 'mode', 'stdev', 'variance', 'correlation', 'linreg',
        'quartiles', 'zscore', 'percentile', 'norm_cdf', 'norm_inv', 'binom_pmf',
        't_cdf', 'chi2_cdf', 'poisson_pmf',
        'nCr', 'nPr', 'gcd', 'lcm', 'prime_factors', 'is_prime',
        'convert_length', 'convert_mass', 'convert_temp', 'convert_time',
        'c_to_f', 'f_to_c', 'c_to_k', 'k_to_c',
        'fraction', 'dec_to_frac', 'mixed', 'ratio', 'proportion',
        'const', 'AND', 'OR', 'NOT', 'XOR',
        'percent', 'pct', 'percent', 'pct', 'percent_add', 'percent_sub', 'percent_of',
        'percent_change', 'percent_diff', 'pct_add', 'pct_sub', 'pct_of',
        'pct_change', 'pct_diff'
    ]
    
    STRING_ARG_FUNCTIONS = [
        'derivative', 'diff', 'integrate', 'integral', 'solve', 'roots', 
        'summation', 'sigma', 'product', 'solve_inequality'
    ]
    
    @staticmethod
    def auto_fix_function_strings(expr):
        """Auto-add quotes to function arguments that need strings"""
        result = expr
        
        for func in CalculationEngine.STRING_ARG_FUNCTIONS:
            if func + '(' not in result:
                continue
                
            idx = 0
            while True:
                idx = result.find(f'{func}(', idx)
                if idx == -1:
                    break
                
                paren_start = idx + len(func)
                paren_count = 0
                i = paren_start
                arg_start = paren_start + 1
                arg_end = -1
                
                while i < len(result):
                    if result[i] == '(':
                        paren_count += 1
                    elif result[i] == ')':
                        paren_count -= 1
                        if paren_count == 0:
                            arg_end = i
                            break
                    elif result[i] == ',' and paren_count == 1:
                        arg_end = i
                        break
                    i += 1
                
                if arg_end == -1:
                    break
                
                arg = result[arg_start:arg_end].strip()
                
                if (arg.startswith('"') and arg.endswith('"')) or \
                   (arg.startswith("'") and arg.endswith("'")):
                    idx = arg_end
                    continue
                
                if any(char in arg for char in ['*', '+', '-', '/', 'x', '^', 'i', ' ']):
                    result = result[:arg_start] + f'"{arg}"' + result[arg_end:]
                    idx = arg_end + 2  
                else:
                    idx = arg_end
        
        return result
    
    @staticmethod
    def fix_implicit_multiplication(expr):
        
        expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
        
        expr = re.sub(r'\)([a-zA-Z(])', r')*\1', expr)
        
        pattern = r'([a-zA-Z_][a-zA-Z0-9_]*)(\()'
        
        def check_function(match):
            func_name = match.group(1)
            if func_name in CalculationEngine.KNOWN_FUNCTIONS:
                return match.group(0)
            if len(func_name) == 1:
                return f'{func_name}*('
            return match.group(0)
        
        expr = re.sub(pattern, check_function, expr)
        
        return expr
    
    @staticmethod
    def process_and_calculate(expr, formatter):
        if not expr:
            return None, "0"
        
        calc_expr = expr.replace('×', '*').replace('÷', '/')
        
        calc_expr = CalculationEngine.fix_implicit_multiplication(calc_expr)
        
        calc_expr = CalculationEngine.auto_fix_function_strings(calc_expr)
        
        print(f"Original: {expr}")
        print(f"Calculating: {calc_expr}")
        
        result = calculate(calc_expr)
        
        formatted_result = formatter.format_result(result)
        
        return result, formatted_result