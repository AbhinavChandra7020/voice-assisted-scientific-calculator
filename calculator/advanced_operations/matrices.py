import numpy as np

def is_matrix(obj):
    if not isinstance(obj, list):
        return False
    if len(obj) == 0:
        return False
    return all(isinstance(row, list) for row in obj)

def to_numpy(matrix):
    
    return np.array(matrix)

def from_numpy(array):
    
    return array.tolist()

# Matrix creation functions
def matrix_create(rows, cols, fill=0):

    return [[fill for _ in range(cols)] for _ in range(rows)]

def identity(n):
    
    result = np.eye(n)
    return from_numpy(result)

def zero_matrix(rows, cols):

    result = np.zeros((rows, cols))
    return from_numpy(result)

def ones_matrix(rows, cols):
    
    result = np.ones((rows, cols))
    return from_numpy(result)

# matrix operations
def matrix_add(A, B):

    A_np = to_numpy(A)
    B_np = to_numpy(B)
    result = A_np + B_np
    return from_numpy(result)

def matrix_subtract(A, B):

    A_np = to_numpy(A)
    B_np = to_numpy(B)
    result = A_np - B_np
    return from_numpy(result)

def matrix_multiply(A, B):

    A_np = to_numpy(A)
    B_np = to_numpy(B)
    result = A_np @ B_np  # @ is matrix multiplication operator
    return from_numpy(result)

def matrix_scalar_multiply(matrix, scalar):

    M = to_numpy(matrix)
    result = scalar * M
    return from_numpy(result)

def transpose(matrix):
    
    M = to_numpy(matrix)
    result = M.T
    return from_numpy(result)

def determinant(matrix):

    M = to_numpy(matrix)
    if M.shape[0] != M.shape[1]:
        raise ValueError("Determinant requires a square matrix")
    result = np.linalg.det(M)
    return float(result)

def inverse(matrix):

    M = to_numpy(matrix)
    if M.shape[0] != M.shape[1]:
        raise ValueError("Inverse requires a square matrix")
    result = np.linalg.inv(M)
    return from_numpy(result)

def trace(matrix):

    M = to_numpy(matrix)
    result = np.trace(M)
    return float(result)

def rank(matrix):

    M = to_numpy(matrix)
    result = np.linalg.matrix_rank(M)
    return int(result)

def eigenvalues(matrix):
 
    M = to_numpy(matrix)
    if M.shape[0] != M.shape[1]:
        raise ValueError("Eigenvalues require a square matrix")
    result = np.linalg.eigvals(M)
    return from_numpy(result)

def matrix_power(matrix, n):

    M = to_numpy(matrix)
    result = np.linalg.matrix_power(M, int(n))
    return from_numpy(result)

MATRIX_FUNCTIONS = {
    'identity': identity,
    'eye': identity, 
    'zeros': zero_matrix,
    'ones': ones_matrix,
    
    'matmul': matrix_multiply,
    'transpose': transpose,
    'det': determinant,
    'determinant': determinant,
    'inv': inverse,
    'inverse': inverse,
    'trace': trace,
    'rank': rank,
    'eigenvalues': eigenvalues,
    'eigvals': eigenvalues,  
    'matrix_power': matrix_power,
    'matpow': matrix_power,  
}

def get_function(name):
    """Get a matrix function by name"""
    if name in MATRIX_FUNCTIONS:
        return MATRIX_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown matrix function: {name}")