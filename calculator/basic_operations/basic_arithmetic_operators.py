import ast

def apply_operator(op, left, right):

    # avoiding circular imports
    from ..advanced_operations.matrices import is_matrix, matrix_add, matrix_subtract, matrix_multiply, matrix_scalar_multiply, matrix_power
    from ..advanced_operations.vectors import is_vector, add_vectors, subtract_vectors, scalar_multiply as vector_scalar_multiply, dot
    
    left_is_matrix = is_matrix(left)
    right_is_matrix = is_matrix(right)
    left_is_vector = is_vector(left) and not left_is_matrix
    right_is_vector = is_vector(right) and not right_is_matrix
    
    # matrix operations
    if left_is_matrix and right_is_matrix:
        if isinstance(op, ast.Add):
            return matrix_add(left, right)
        elif isinstance(op, ast.Sub):
            return matrix_subtract(left, right)
        elif isinstance(op, ast.Mult):
            return matrix_multiply(left, right)
        elif isinstance(op, ast.Pow):
            return matrix_power(left, right)
        else:
            raise ValueError(f"Unsupported matrix operator: {type(op).__name__}")
    
    # vector operations
    elif left_is_vector and right_is_vector:
        if isinstance(op, ast.Add):
            return add_vectors(left, right)
        elif isinstance(op, ast.Sub):
            return subtract_vectors(left, right)
        elif isinstance(op, ast.Mult):
            # dot product
            return dot(left, right)
        else:
            raise ValueError(f"Unsupported vector operator: {type(op).__name__}")
    
    # matrix operations
    elif left_is_matrix or right_is_matrix:
        if isinstance(op, ast.Mult):
            if left_is_matrix:
                return matrix_scalar_multiply(left, right)
            else:
                return matrix_scalar_multiply(right, left)
        else:
            raise ValueError(f"Cannot apply {type(op).__name__} between scalar and matrix")
    
    # vector operations (scalar)
    elif left_is_vector or right_is_vector:
        if isinstance(op, ast.Mult):
            if left_is_vector:
                return vector_scalar_multiply(left, right)
            else:
                return vector_scalar_multiply(right, left)
        else:
            raise ValueError(f"Cannot apply {type(op).__name__} between scalar and vector")
    
    # basic arithmetic
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
        # handle matrix/vector negation
        from ..advanced_operations.matrices import is_matrix, matrix_scalar_multiply
        from ..advanced_operations.vectors import is_vector, scalar_multiply as vector_scalar_multiply
        
        if is_matrix(operand):
            return matrix_scalar_multiply(operand, -1)
        elif is_vector(operand):
            return vector_scalar_multiply(operand, -1)
        return -operand
    else:
        raise ValueError(f"Unsupported unary operator: {type(op).__name__}")