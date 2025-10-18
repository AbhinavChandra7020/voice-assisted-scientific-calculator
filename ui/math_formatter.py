import re


class MathFormatter:
    
    @staticmethod
    def format_expression(expr):
        if not expr:
            return ""
        
        result = expr
        
        result = re.sub(r'percent_add\(([^,]+),\s*([^)]+)\)', r'\1 + \2%', result)
        result = re.sub(r'pct_add\(([^,]+),\s*([^)]+)\)', r'\1 + \2%', result)
        result = re.sub(r'percent_sub\(([^,]+),\s*([^)]+)\)', r'\1 - \2%', result)
        result = re.sub(r'pct_sub\(([^,]+),\s*([^)]+)\)', r'\1 - \2%', result)
        result = re.sub(r'percent_of\(([^,]+),\s*([^)]+)\)', r'\2% of \1', result)
        result = re.sub(r'pct_of\(([^,]+),\s*([^)]+)\)', r'\2% of \1', result)
        result = re.sub(r'percent\(([^)]+)\)', r'\1%', result)
        result = re.sub(r'pct\(([^)]+)\)', r'\1%', result)
        
        result = re.sub(r'sqrt\(([^)]+)\)', r'√(\1)', result)
        result = re.sub(r'cbrt\(([^)]+)\)', r'∛(\1)', result)
        result = re.sub(r'derivative\(([^,]+),\s*([^)]+)\)', r'd/dx(\1)|ₓ₌\2', result)
        result = re.sub(r'integrate\(([^,]+),\s*([^,]+),\s*([^)]+)\)', r'∫\2→\3(\1)dx', result)
        result = re.sub(r'summation\(([^,]+),\s*([^,]+),\s*([^)]+)\)', r'Σ[\2→\3](\1)', result)
        
        result = result.replace('pi', 'π')
        result = result.replace('phi', 'φ')
        
        result = result.replace('**', '^')
        result = result.replace('*', '×')
        result = result.replace('/', '÷')
        
        result = re.sub(r'\^2(?!\d)', '²', result)
        result = re.sub(r'\^3(?!\d)', '³', result)
        
        return result
    
    @staticmethod
    def format_result(result):
        if isinstance(result, list):
            if all(isinstance(row, list) for row in result):
                return MathFormatter.format_matrix(result)
            return str(result)
        elif isinstance(result, complex):
            return MathFormatter.format_complex(result)
        elif isinstance(result, float):
            if result.is_integer():
                return str(int(result))
            return f"{result:.10g}"
        else:
            return str(result)
    
    @staticmethod
    def format_matrix(matrix):
        if not matrix:
            return "[]"
        
        str_matrix = [[str(cell) for cell in row] for row in matrix]
        col_widths = [max(len(str_matrix[r][c]) for r in range(len(matrix))) 
                      for c in range(len(matrix[0]))]
        
        lines = []
        for i, row in enumerate(str_matrix):
            formatted_row = "  ".join(cell.rjust(col_widths[j]) 
                                      for j, cell in enumerate(row))
            if i == 0:
                lines.append(f"┌ {formatted_row} ┐")
            elif i == len(matrix) - 1:
                lines.append(f"└ {formatted_row} ┘")
            else:
                lines.append(f"│ {formatted_row} │")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_complex(num):
        real, imag = num.real, num.imag
        if real == 0:
            return f"{imag}i"
        elif imag == 0:
            return str(real)
        elif imag > 0:
            return f"{real}+{imag}i"
        else:
            return f"{real}{imag}i"