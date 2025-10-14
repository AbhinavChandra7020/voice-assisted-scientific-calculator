# evlution parser and program initializer with checks
import ast
from .basic_operations.basic_arithmetic_operators import apply_operator, apply_unary_operator
from .basic_operations.basic_functions import get_function as get_basic_function
from .advanced_operations.advanced_functions import get_function as get_advanced_function
from .advanced_operations.complex_numbers import get_function as get_complex_function
from .advanced_operations.calculus import get_function as get_calculus_function, init_calculus
from .advanced_operations.matrices import get_function as get_matrix_function
from .advanced_operations.vectors import get_function as get_vector_function
from .advanced_operations.solver import get_function as get_solver_function, init_solver
from .advanced_operations.statistics import get_function as get_statistics_function
from .constants.constant_values import get_constant
from .basic_operations.random_functions import get_function as get_random_function
from .constants.physical_constants import get_function as get_physical_function
from .constants.base_conversion import get_function as get_base_function
from .advanced_operations.summation import get_function as get_summation_function, init_summation
from .basic_operations.unit_conversions import get_function as get_unit_function
from .basic_operations.fractions_calc import get_function as get_fraction_function
from .advanced_operations.probability import get_function as get_probability_function
from .utils.history import get_function as get_history_function, add_to_history
from .basic_operations.ratio_functions import get_function as get_ratio_function
from .basic_operations.logical_operators import get_function as get_logical_function
from .advanced_operations.inequality_solver import get_function as get_inequality_function

_last_answer = 0

def get_ans():
    return _last_answer

def set_ans(value):
    global _last_answer
    _last_answer = value

def get_function(name):
    for getter in [get_basic_function, get_advanced_function, 
                   get_complex_function, get_calculus_function,
                   get_matrix_function, get_vector_function,
                   get_solver_function, get_statistics_function,
                   get_random_function, get_physical_function,
                   get_base_function, get_summation_function,
                   get_unit_function, get_fraction_function,
                   get_probability_function, get_history_function,
                   get_ratio_function, get_logical_function,
                   get_inequality_function]:
        try:
            return getter(name)
        except ValueError:
            continue
    
    raise ValueError(f"Unknown function: {name}")
    
def eval_node(node):

    if isinstance(node, ast.Constant):
        return node.value
    
    elif isinstance(node, ast.List):
        return [eval_node(element) for element in node.elts]
    
    elif isinstance(node, ast.BinOp):
        left = eval_node(node.left)
        right = eval_node(node.right)
        return apply_operator(node.op, left, right)
    
    elif isinstance(node, ast.UnaryOp):
        operand = eval_node(node.operand)
        return apply_unary_operator(node.op, operand)
    
    elif isinstance(node, ast.Call):
        func_name = node.func.id
        func = get_function(func_name)
        args = [eval_node(arg) for arg in node.args]
        return func(*args)
    
    elif isinstance(node, ast.Name):
        return get_constant(node.id)
    
    else:
        raise ValueError(f"Unsupported operation: {type(node).__name__}")

def calculate_multi(expression):

    statements = expression.split(':')
    results = []
    
    for stmt in statements:
        stmt = stmt.strip()
        if stmt:
            result = calculate(stmt)
            results.append(result)
    
    return results

def calculate(expression):

    if ':' in expression:
        return calculate_multi(expression)
    
    try:
        tree = ast.parse(expression, mode='eval')
        result = eval_node(tree.body)
        
        if isinstance(result, (int, float, complex)):
            set_ans(result)
        
        add_to_history(expression, result)
        
        return result
    
    except Exception as e:
        return f"Error: {str(e)}"

# start the engines
init_calculus(eval_node)
init_solver(eval_node)
init_summation(eval_node)