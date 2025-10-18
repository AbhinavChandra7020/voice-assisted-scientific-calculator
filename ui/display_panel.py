import tkinter as tk
from tkinter import font as tkfont


class DisplayPanel:
    
    def __init__(self, parent_frame, parent):
        self.parent = parent
        self.display_frame = tk.Frame(
            parent_frame, 
            bg='#1e272e',
            relief='flat',
            bd=0
        )
        self.display_frame.pack(fill='x', padx=15, pady=10)
        
        self.inner_frame = tk.Frame(
            self.display_frame,
            bg='#1e272e',
            highlightthickness=2,
            highlightbackground='#5f27cd',
            highlightcolor='#5f27cd'
        )
        self.inner_frame.pack(fill='both', padx=3, pady=3)
        
        self.create_math_display()
        self.create_expression_entry()
        self.create_result_display()
    
    def create_math_display(self):
        self.math_display = tk.Label(
            self.inner_frame, 
            text="", 
            font=("Segoe UI", 13),
            bg='#1e272e', 
            fg='#00d2d3', 
            anchor='w', 
            justify='left', 
            height=2,
            padx=10
        )
        self.math_display.pack(fill='x', pady=(10, 0))
    
    def create_expression_entry(self):
        entry_font = tkfont.Font(family="Consolas", size=15)
        self.expression_entry = tk.Entry(
            self.inner_frame, 
            font=entry_font,
            bg='#2f3640', 
            fg='#f1f2f6', 
            insertbackground='#5f27cd',  # Purple cursor
            insertwidth=3,
            relief='flat', 
            bd=0,
            highlightthickness=0
        )
        self.expression_entry.pack(fill='x', padx=10, pady=8)
        self.expression_entry.bind('<KeyRelease>', self.parent.on_entry_change)
        self.expression_entry.bind('<Return>', lambda e: self.parent.calculate_result())
        self.expression_entry.bind('<BackSpace>', self.parent.on_backspace)
    
    def create_result_display(self):
        result_font = tkfont.Font(family="Consolas", size=24, weight="bold")
        self.result_display = tk.Text(
            self.inner_frame, 
            font=result_font,
            bg='#1e272e', 
            fg='#ffffff', 
            height=2, 
            state='disabled', 
            relief='flat',
            bd=0,
            highlightthickness=0,
            padx=10
        )
        self.result_display.pack(fill='x', pady=(0, 10))