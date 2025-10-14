import ast

class SummationEngine:
    
    def __init__(self, parser_eval_node):
        self.eval_node = parser_eval_node
    
    def make_function(self, expression_str, var_name='i'):
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
    
    def summation(self, expression, var='i', start=1, end=10):

        start = int(start)
        end = int(end)
        
        func = self.make_function(expression, var)
        
        result = 0
        for i in range(start, end + 1):
            result += func(i)
        
        return result
    
    def product(self, expression, var='i', start=1, end=5):

        start = int(start)
        end = int(end)
        
        func = self.make_function(expression, var)
        
        result = 1
        for i in range(start, end + 1):
            result *= func(i)
        
        return result


# Global summation engine
summation_engine = None

def init_summation(parser_eval_node):
    global summation_engine
    summation_engine = SummationEngine(parser_eval_node)

def summation(expression, start=1, end=10, var='i'):

    if summation_engine is None:
        raise RuntimeError("Summation engine not initialized")
    return summation_engine.summation(expression, var, start, end)

def product(expression, start=1, end=5, var='i'):

    if summation_engine is None:
        raise RuntimeError("Summation engine not initialized")
    return summation_engine.product(expression, var, start, end)

def sigma(expression, start=1, end=10, var='i'):
    return summation(expression, start, end, var)


SUMMATION_FUNCTIONS = {
    'summation': summation,
    'sum_range': summation,  
    'sigma': sigma,
    'product': product,
    'prod': product,  
}

def get_function(name):
    """Get a summation function by name"""
    if name in SUMMATION_FUNCTIONS:
        return SUMMATION_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown summation function: {name}")