import tkinter as tk
from tkinter import ttk


class FunctionTabs:
    
    def __init__(self, parent_frame, parent):
        self.parent = parent
        self.notebook = ttk.Notebook(parent_frame)
        self.notebook.pack(fill='both', expand=True, padx=15, pady=10)
        
        self._configure_modern_style()
        
        self.create_tabs()
    
    def _configure_modern_style(self):
        style = ttk.Style()
        
        style.theme_use('clam')
        style.configure('TNotebook', 
                       background='#2a2a2a',
                       borderwidth=0,
                       tabmargins=[2, 5, 2, 0])
        
        style.configure('TNotebook.Tab',
                       background='#3a3a3a',
                       foreground='white',
                       padding=[20, 10],
                       borderwidth=0,
                       focuscolor='none')
        
        style.map('TNotebook.Tab',
                 background=[('selected', '#5f27cd')],
                 foreground=[('selected', 'white')],
                 expand=[('selected', [1, 1, 1, 0])])
    
    def create_tabs(self):
        tabs_config = [
            ('Basic', self.create_basic_functions),
            ('Advanced', self.create_advanced_functions),
            ('Statistics', self.create_statistics_functions),
            ('Matrix', self.create_matrix_functions)
        ]
        
        for tab_name, create_func in tabs_config:
            tab = tk.Frame(self.notebook, bg='#2a2a2a')
            self.notebook.add(tab, text=tab_name)
            create_func(tab)
    
    def create_basic_functions(self, parent):
        functions = [
            ['sin(', 'cos(', 'tan(', 'log(', 'ln('],
            ['asin(', 'acos(', 'atan(', 'log2(', 'exp('],
            ['sqrt(', 'cbrt(', 'abs(', 'factorial(', 'nthroot('],
            ['sinh(', 'cosh(', 'tanh(', 'floor(', 'ceil('],
            ['percent(', 'pct_add(', 'pct_sub(', 'pct_of(', 'pct_change('],
        ]
        
        self._create_modern_button_grid(parent, functions, '#54a0ff', '#2e86de')
    
    def create_advanced_functions(self, parent):
        functions = [
            ['derivative(', 'integrate(', 'summation(', 'solve(', 'roots('],
            ['nCr(', 'nPr(', 'gcd(', 'lcm(', 'is_prime('],
            ['prime_factors(', 'rect_to_polar(', 'polar_to_rect(', 'fraction(', 'dec_to_frac('],
            [',', 'ans', 'pi', 'e', 'phi'],
        ]
        
        self._create_modern_button_grid(parent, functions, '#ff6348', '#ff4757')
    
    def create_statistics_functions(self, parent):
        functions = [
            ['mean(', 'median(', 'mode(', 'stdev(', 'variance('],
            ['correlation(', 'linreg(', 'quartiles(', 'zscore(', 'percentile('],
            ['norm_cdf(', 'norm_inv(', 'binom_pmf(', 't_cdf(', 'chi2_cdf('],
        ]
        
        self._create_modern_button_grid(parent, functions, '#1dd1a1', '#10ac84')
    
    def create_matrix_functions(self, parent):
        functions = [
            ['det(', 'transpose(', 'inv(', 'trace(', 'rank('],
            ['magnitude(', 'dot(', 'cross(', 'normalize(', 'distance('],
            ['[', ']', ',', '[[', ']]'],
        ]
        
        self._create_modern_button_grid(parent, functions, '#feca57', '#ff9ff3')
    
    def _create_modern_button_grid(self, parent, functions, bg_color, hover_color):
        for row in functions:
            frame = tk.Frame(parent, bg='#2a2a2a')
            frame.pack(fill='x', pady=3, padx=5)
            
            for func in row:
                btn = tk.Button(
                    frame, text=func,
                    font=("Segoe UI", 10, "bold"),
                    bg=bg_color,
                    fg='white',
                    activebackground=hover_color,
                    activeforeground='white',
                    relief='flat',
                    bd=0,
                    cursor='hand2',
                    height=2,
                    command=lambda f=func: self.parent.insert_text(f)
                )
                btn.pack(side='left', padx=2, expand=True, fill='x')
                
                btn.bind('<Enter>', lambda e, b=btn, h=hover_color: b.config(bg=h))
                btn.bind('<Leave>', lambda e, b=btn, c=bg_color: b.config(bg=c))