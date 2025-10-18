import tkinter as tk


class MenuBar:
    
    def __init__(self, root, parent):
        self.root = root
        self.parent = parent
        self.create_menu()
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        self._create_mode_menu(menubar)
        self._create_functions_menu(menubar)
        self._create_constants_menu(menubar)
        self._create_help_menu(menubar)
    
    def _create_mode_menu(self, menubar):
        mode_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Mode", menu=mode_menu)
        mode_menu.add_command(label="Degrees (DEG)", 
                            command=lambda: self.parent.set_angle_mode('DEG'))
        mode_menu.add_command(label="Radians (RAD)", 
                            command=lambda: self.parent.set_angle_mode('RAD'))
        mode_menu.add_separator()
        mode_menu.add_command(label="Clear History", 
                            command=self.parent.clear_history)
    
    def _create_functions_menu(self, menubar):
        func_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Functions", menu=func_menu)
        
        self._create_basic_submenu(func_menu)
        
        self._create_percent_submenu(func_menu)
        
        self._create_trig_submenu(func_menu)
        
        self._create_calculus_submenu(func_menu)
        
        self._create_matrix_submenu(func_menu)
        
        self._create_statistics_submenu(func_menu)
        
        self._create_conversions_submenu(func_menu)
    
    def _create_basic_submenu(self, parent_menu):
        basic_menu = tk.Menu(parent_menu, tearoff=0)
        parent_menu.add_cascade(label="Basic", menu=basic_menu)
        basic_menu.add_command(label="abs()", 
                             command=lambda: self.parent.insert_function('abs'))
        basic_menu.add_command(label="sqrt()", 
                             command=lambda: self.parent.insert_function('sqrt'))
        basic_menu.add_command(label="cbrt()", 
                             command=lambda: self.parent.insert_function('cbrt'))
        basic_menu.add_command(label="factorial()", 
                             command=lambda: self.parent.insert_function('factorial'))
    
    def _create_percent_submenu(self, parent_menu):
        percent_menu = tk.Menu(parent_menu, tearoff=0)
        parent_menu.add_cascade(label="Percentage", menu=percent_menu)
        percent_menu.add_command(label="percent(x) - to decimal", 
                               command=lambda: self.parent.insert_function('percent'))
        percent_menu.add_command(label="percent_add(base, pct)", 
                               command=lambda: self.parent.insert_text('percent_add('))
        percent_menu.add_command(label="percent_sub(base, pct)", 
                               command=lambda: self.parent.insert_text('percent_sub('))
        percent_menu.add_command(label="percent_of(base, pct)", 
                               command=lambda: self.parent.insert_text('percent_of('))
        percent_menu.add_command(label="percent_change(old, new)", 
                               command=lambda: self.parent.insert_text('percent_change('))
        percent_menu.add_command(label="percent_diff(v1, v2)", 
                               command=lambda: self.parent.insert_text('percent_diff('))
    
    def _create_trig_submenu(self, parent_menu):
        trig_menu = tk.Menu(parent_menu, tearoff=0)
        parent_menu.add_cascade(label="Trigonometric", menu=trig_menu)
        for func in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh']:
            trig_menu.add_command(label=f"{func}()", 
                                command=lambda f=func: self.parent.insert_function(f))
    
    def _create_calculus_submenu(self, parent_menu):
        calc_menu = tk.Menu(parent_menu, tearoff=0)
        parent_menu.add_cascade(label="Calculus", menu=calc_menu)
        calc_menu.add_command(label="derivative(expr, at)", 
                            command=lambda: self.parent.insert_text('derivative('))
        calc_menu.add_command(label="integrate(expr, lower, upper)", 
                            command=lambda: self.parent.insert_text('integrate('))
        calc_menu.add_command(label="summation(expr, start, end)", 
                            command=lambda: self.parent.insert_text('summation('))
    
    def _create_matrix_submenu(self, parent_menu):
        matrix_menu = tk.Menu(parent_menu, tearoff=0)
        parent_menu.add_cascade(label="Matrix & Vector", menu=matrix_menu)
        matrix_menu.add_command(label="det()", 
                              command=lambda: self.parent.insert_function('det'))
        matrix_menu.add_command(label="transpose()", 
                              command=lambda: self.parent.insert_function('transpose'))
        matrix_menu.add_command(label="inv()", 
                              command=lambda: self.parent.insert_function('inv'))
        matrix_menu.add_command(label="magnitude()", 
                              command=lambda: self.parent.insert_function('magnitude'))
        matrix_menu.add_command(label="dot()", 
                              command=lambda: self.parent.insert_function('dot'))
        matrix_menu.add_command(label="cross()", 
                              command=lambda: self.parent.insert_function('cross'))
    
    def _create_statistics_submenu(self, parent_menu):
        stats_menu = tk.Menu(parent_menu, tearoff=0)
        parent_menu.add_cascade(label="Statistics", menu=stats_menu)
        for func in ['mean', 'median', 'mode', 'stdev', 'variance', 'correlation']:
            stats_menu.add_command(label=f"{func}()", 
                                 command=lambda f=func: self.parent.insert_function(f))
    
    def _create_conversions_submenu(self, parent_menu):
        conv_menu = tk.Menu(parent_menu, tearoff=0)
        parent_menu.add_cascade(label="Conversions", menu=conv_menu)
        conv_menu.add_command(label="convert_length()", 
                            command=lambda: self.parent.insert_text('convert_length('))
        conv_menu.add_command(label="convert_mass()", 
                            command=lambda: self.parent.insert_text('convert_mass('))
        conv_menu.add_command(label="convert_temp()", 
                            command=lambda: self.parent.insert_text('convert_temp('))
        conv_menu.add_command(label="c_to_f()", 
                            command=lambda: self.parent.insert_function('c_to_f'))
        conv_menu.add_command(label="f_to_c()", 
                            command=lambda: self.parent.insert_function('f_to_c'))
    
    def _create_constants_menu(self, menubar):
        const_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Constants", menu=const_menu)
        const_menu.add_command(label="π (pi)", 
                             command=lambda: self.parent.insert_text('pi'))
        const_menu.add_command(label="e", 
                             command=lambda: self.parent.insert_text('e'))
        const_menu.add_command(label="φ (phi)", 
                             command=lambda: self.parent.insert_text('phi'))
        const_menu.add_separator()
        const_menu.add_command(label="Speed of light (c)", 
                             command=lambda: self.parent.insert_text('const("c")'))
        const_menu.add_command(label="Planck constant (h)", 
                             command=lambda: self.parent.insert_text('const("h")'))
        const_menu.add_command(label="Gravitational constant (G)", 
                             command=lambda: self.parent.insert_text('const("G")'))
    
    def _create_help_menu(self, menubar):
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Quick Guide", 
                            command=self.parent.show_quick_guide)
        help_menu.add_command(label="About", 
                            command=self.parent.show_about)