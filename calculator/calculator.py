import math
import ast

def eval_node(node):

    if isinstance(node, ast.Constant):
        return node.value
    
    elif isinstance(node, ast.BinOp):
        left = eval_node(node.left)
        right = eval_node(node.right)

        return apply_operator(node.op, left, right)
    
    elif isinstance(node, ast.UnaryOp):
        operand = eval_node(node.operand)

        return apply_unary_operator(node.op, operand) 

def calculate(expression):

    try:
        tree = ast.parse(expression, mode='eval')
        result  = eval_node(tree.body)

        return result
    
    except Exception as e:
        return f"Error: {str(e)}"
    
def apply_operator(op, left, right):
 
    if isinstance(op, ast.Add):
        return left + right
    elif isinstance(op, ast.Sub):
        return left - right
    elif isinstance(op, ast.Mult):
        return left * right
    elif isinstance(op, ast.Div):
        if right == 0:
            raise ValueError("Division by zero")
        return left / right
    elif isinstance(op, ast.Pow):
        return left ** right
    elif isinstance(op, ast.Mod):
        return left % right
    elif isinstance(op, ast.FloorDiv):
        return left // right
    else:
        raise ValueError(f"Unsupported operator: {type(op).__name__}")
    
def apply_unary_operator(op, operand):

    if isinstance(op, ast.UAdd):  
        return +operand
    elif isinstance(op, ast.USub):  
        return -operand
    else:
        raise ValueError(f"Unsupported unary operator: {type(op).__name__}")
