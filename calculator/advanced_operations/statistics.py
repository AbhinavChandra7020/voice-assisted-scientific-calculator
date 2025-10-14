import math
from collections import Counter

def validate_data(data):
    if not isinstance(data, list):
        raise ValueError("Data must be a list")
    if len(data) == 0:
        raise ValueError("Data list cannot be empty")
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError(f"All data must be numbers, found: {type(item)}")

def mean(data):

    validate_data(data)
    return sum(data) / len(data)

def median(data):

    validate_data(data)
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]

def mode(data):

    validate_data(data)
    counter = Counter(data)
    max_count = max(counter.values())
    modes = [value for value, count in counter.items() if count == max_count]
    
    if len(modes) == 1:
        return modes[0]
    else:
        return modes

def data_range(data):

    validate_data(data)
    return max(data) - min(data)

def data_sum(data):

    validate_data(data)
    return sum(data)

def data_min(data):

    validate_data(data)
    return min(data)

def data_max(data):

    validate_data(data)
    return max(data)

def count(data):

    validate_data(data)
    return len(data)

def variance(data, sample=True):

    validate_data(data)
    n = len(data)
    if n < 2 and sample:
        raise ValueError("Sample variance requires at least 2 data points")
    
    avg = mean(data)
    squared_diffs = [(x - avg) ** 2 for x in data]
    
    if sample:
        return sum(squared_diffs) / (n - 1)  
    else:
        return sum(squared_diffs) / n  

def stdev(data, sample=True):

    return math.sqrt(variance(data, sample))

def std(data, sample=True):
    """Alias for stdev"""
    return stdev(data, sample)

def percentile(data, p):

    validate_data(data)
    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    k = (n - 1) * p / 100
    f = math.floor(k)
    c = math.ceil(k)
    
    if f == c:
        return sorted_data[int(k)]
    
    d0 = sorted_data[int(f)] * (c - k)
    d1 = sorted_data[int(c)] * (k - f)
    return d0 + d1

def quartiles(data):

    validate_data(data)
    return [
        percentile(data, 25),  
        percentile(data, 50),  
        percentile(data, 75)   
    ]

def iqr(data):

    q = quartiles(data)
    return q[2] - q[0]

def covariance(x_data, y_data, sample=True):

    validate_data(x_data)
    validate_data(y_data)
    
    if len(x_data) != len(y_data):
        raise ValueError("Both datasets must have the same length")
    
    n = len(x_data)
    if n < 2 and sample:
        raise ValueError("Sample covariance requires at least 2 data points")
    
    mean_x = mean(x_data)
    mean_y = mean(y_data)
    
    cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_data, y_data))
    
    if sample:
        return cov / (n - 1)
    else:
        return cov / n

def correlation(x_data, y_data):

    validate_data(x_data)
    validate_data(y_data)
    
    if len(x_data) != len(y_data):
        raise ValueError("Both datasets must have the same length")
    
    cov = covariance(x_data, y_data)
    std_x = stdev(x_data)
    std_y = stdev(y_data)
    
    if std_x == 0 or std_y == 0:
        raise ValueError("Cannot calculate correlation with zero variance")
    
    return cov / (std_x * std_y)

def linear_regression(x_data, y_data):

    validate_data(x_data)
    validate_data(y_data)
    
    if len(x_data) != len(y_data):
        raise ValueError("Both datasets must have the same length")
    
    n = len(x_data)
    mean_x = mean(x_data)
    mean_y = mean(y_data)
    
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_data, y_data))
    denominator = sum((x - mean_x) ** 2 for x in x_data)
    
    if denominator == 0:
        raise ValueError("Cannot calculate regression with constant x values")
    
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x
    
    return (slope, intercept)

def zscore(data, value):

    validate_data(data)
    avg = mean(data)
    sd = stdev(data)
    
    if sd == 0:
        raise ValueError("Cannot calculate z-score with zero standard deviation")
    
    return (value - avg) / sd


STATISTICS_FUNCTIONS = {
    # basic statistics
    'mean': mean,
    'avg': mean,  
    'average': mean,  
    'median': median,
    'mode': mode,
    'range': data_range,
    'sum': data_sum,
    'min': data_min,
    'max': data_max,
    'count': count,
    'len': count,  
    
    'variance': variance,
    'var': variance,  
    'stdev': stdev,
    'std': std,
    'stddev': std,  
    
    'percentile': percentile,
    'quartiles': quartiles,
    'iqr': iqr,
    
    'covariance': covariance,
    'cov': covariance,  # Alias
    'correlation': correlation,
    'corr': correlation,  # Alias
    'linreg': linear_regression,
    'regression': linear_regression,
    'zscore': zscore,
}

def get_function(name):
    if name in STATISTICS_FUNCTIONS:
        return STATISTICS_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown statistical function: {name}")