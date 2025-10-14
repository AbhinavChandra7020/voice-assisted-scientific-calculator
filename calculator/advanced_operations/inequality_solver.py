import sympy as sp
from sympy import symbols, solve_univariate_inequality, S

def solve_inequality(inequality_str, var='x'):

    try:
        x = symbols(var)
        
        inequality_str = inequality_str.replace('<=', '≤')
        inequality_str = inequality_str.replace('>=', '≥')
        inequality_str = inequality_str.replace('!=', '≠')
        
        if '<' in inequality_str or '≤' in inequality_str:
            if '≤' in inequality_str:
                parts = inequality_str.split('≤')
                expr = sp.sympify(parts[0]) - sp.sympify(parts[1])
                ineq = expr <= 0
            else:
                parts = inequality_str.split('<')
                expr = sp.sympify(parts[0]) - sp.sympify(parts[1])
                ineq = expr < 0
        
        elif '>' in inequality_str or '≥' in inequality_str:
            if '≥' in inequality_str:
                parts = inequality_str.split('≥')
                expr = sp.sympify(parts[0]) - sp.sympify(parts[1])
                ineq = expr >= 0
            else:
                parts = inequality_str.split('>')
                expr = sp.sympify(parts[0]) - sp.sympify(parts[1])
                ineq = expr > 0
        
        elif '≠' in inequality_str:
            parts = inequality_str.split('≠')
            expr = sp.sympify(parts[0]) - sp.sympify(parts[1])
            ineq = sp.Ne(expr, 0)
        
        else:
            raise ValueError("No inequality operator found")
        
        solution = solve_univariate_inequality(ineq, x, relational=False)
        
        return solution
    
    except Exception as e:
        raise ValueError(f"Could not solve inequality: {str(e)}")

def solve_system_inequalities(inequalities, var='x'):

    x = symbols(var)
    solutions = []
    
    for ineq_str in inequalities:
        sol = solve_inequality(ineq_str, var)
        solutions.append(sol)
    
    result = solutions[0]
    for sol in solutions[1:]:
        result = result.intersect(sol)
    
    return result


INEQUALITY_FUNCTIONS = {
    'solve_ineq': solve_inequality,
    'solve_inequality': solve_inequality,
    'solve_ineq_system': solve_system_inequalities,
}

def get_function(name):
    """Get an inequality solver function by name"""
    if name in INEQUALITY_FUNCTIONS:
        return INEQUALITY_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown inequality function: {name}")