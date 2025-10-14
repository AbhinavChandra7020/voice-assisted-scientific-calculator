import ast
from scipy import integrate, misc
import numpy as np

class CalculusEngine:
    
    def __init__(self, parser_eval_node):
   
        self.eval_node = parser_eval_node
    
    def make_function(self, expression_str, var_name='x'):

        # parse the expression once
        tree = ast.parse(expression_str, mode='eval')
        
        def func(value):
            return self._eval_with_variable(tree.body, var_name, value)
        
        return func
    
    def _eval_with_variable(self, node, var_name, var_value):
  
        # avoid circular import
        from ..parser import eval_node as default_eval
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
    
    def derivative(self, expression, var='x', at_point=None):

        if at_point is None:
            raise ValueError("Must specify a point to evaluate derivative (use 'at' parameter)")
        
        func = self.make_function(expression, var)
        
        h = 1e-5  # small step size
        derivative_value = (func(at_point + h) - func(at_point - h)) / (2 * h)
        
        return derivative_value
    
    def integrate(self, expression, var='x', lower=None, upper=None):

        if lower is None or upper is None:
            raise ValueError("Must specify lower and upper bounds for integration")
        
        func = self.make_function(expression, var)
        
        result, error = integrate.quad(func, lower, upper)
        
        return result


calculus_engine = None

def init_calculus(parser_eval_node):
    global calculus_engine
    calculus_engine = CalculusEngine(parser_eval_node)

def derivative(expression, at):
 
    if calculus_engine is None:
        raise RuntimeError("Calculus engine not initialized")
    return calculus_engine.derivative(expression, at_point=at)

def integrate_func(expression, lower, upper):

    if calculus_engine is None:
        raise RuntimeError("Calculus engine not initialized")
    return calculus_engine.integrate(expression, lower=lower, upper=upper)


CALCULUS_FUNCTIONS = {
    'derivative': derivative,
    'diff': derivative,  
    'integrate': integrate_func,
    'integral': integrate_func,  
}

def get_function(name):
    """Get a calculus function by name"""
    if name in CALCULUS_FUNCTIONS:
        return CALCULUS_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown calculus function: {name}")