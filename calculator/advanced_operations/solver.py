# algebraic and transcendental equations solver
import warnings
import ast
from scipy.optimize import fsolve
import sympy as sp

class EquationSolver:
    
    def __init__(self, parser_eval_node):

        self.eval_node = parser_eval_node
    
    def make_function(self, expression_str, var_name='x'):

        tree = ast.parse(expression_str, mode='eval')
        
        def func(value):

            return self._eval_with_variable(tree.body, var_name, value)
        
        return func
    
    def _eval_with_variable(self, node, var_name, var_value):

        from ..basic_operations.basic_arithmetic_operators import apply_operator, apply_unary_operator
        from ..constants.constant_values import get_constant
        from ..parser import get_function
        
        if isinstance(node, ast.Constant):
            return node.value
        
        elif isinstance(node, ast.Name):
            if node.id == var_name:
                return var_value
            else:
                return get_constant(node.id)
        
        elif isinstance(node, ast.BinOp):
            left = self._eval_with_variable(node.left, var_name, var_value)
            right = self._eval_with_variable(node.right, var_name, var_value)
            return apply_operator(node.op, left, right)
        
        elif isinstance(node, ast.UnaryOp):
            operand = self._eval_with_variable(node.operand, var_name, var_value)
            return apply_unary_operator(node.op, operand)
        
        elif isinstance(node, ast.Call):
            func_name = node.func.id
            func = get_function(func_name)
            args = [self._eval_with_variable(arg, var_name, var_value) for arg in node.args]
            return func(*args)
        
        else:
            raise ValueError(f"Unsupported node type: {type(node).__name__}")
    
    def solve_symbolic(self, expression, var='x'):

        try:
            x = sp.Symbol(var)
            
            expr = sp.sympify(expression)
            
            solutions = sp.solve(expr, x)
            
            result = []
            for sol in solutions:
                if sol.is_real:
                    result.append(float(sol))
                else:
                    result.append(complex(sol))
            
            return result
        except Exception as e:
            return None
    
    def solve_numerical(self, expression, var='x', guess=0):

        func = self.make_function(expression, var)
        
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=RuntimeWarning)
            
            try:
                solution = fsolve(func, guess, full_output=False)[0]
                if abs(func(solution)) < 1e-6:
                    return float(solution)
            except:
                pass
            
            for alt_guess in [0, 1, -1, 10, -10, 100, -100]:
                try:
                    solution = fsolve(func, alt_guess, full_output=False)[0]
                    if abs(func(solution)) < 1e-6:
                        return float(solution)
                except:
                    continue
        
        raise ValueError("Could not find solution")


equation_solver = None

def init_solver(parser_eval_node):
    global equation_solver
    equation_solver = EquationSolver(parser_eval_node)

def solve(expression, var='x', guess=0):

    if equation_solver is None:
        raise RuntimeError("Equation solver not initialized")
    
    symbolic_result = equation_solver.solve_symbolic(expression, var)
    if symbolic_result is not None and len(symbolic_result) > 0:
        return symbolic_result
    
    try:
        root = equation_solver.solve_numerical(expression, var, guess)
        return [root]
    except:
        raise ValueError("Could not find solution")

def solve_for(expression, var='x', guess=0):

    if equation_solver is None:
        raise RuntimeError("Equation solver not initialized")
    
    root = equation_solver.solve_numerical(expression, var, guess)
    return root

def roots(expression, var='x'):

    return solve(expression, var)


SOLVER_FUNCTIONS = {
    'solve': solve,
    'solve_for': solve_for,
    'roots': roots,
}

def get_function(name):
    """Get a solver function by name"""
    if name in SOLVER_FUNCTIONS:
        return SOLVER_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown solver function: {name}")