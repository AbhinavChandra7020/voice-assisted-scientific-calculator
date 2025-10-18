
import tkinter as tk
from tkinter import font as tkfont, scrolledtext

from calculator.utils.angle_modes import angle_mode
from calculator.utils.history import history_manager

from .math_formatter import MathFormatter
from .menu_bar import MenuBar
from .display_panel import DisplayPanel
from .function_tabs import FunctionTabs
from .number_pad import NumberPad
from .voice_handler import VoiceHandler
from .calculation_engine import CalculationEngine
from .ui_helpers import UIHelpers


class CasioCalculatorGUI:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Operated Scientific Calculator")
        self.root.geometry("650x1100")
        self.root.resizable(True, True)
        self.root.configure(bg='#2a2a2a')
        
        self.expression = ""
        
        # Components
        self.formatter = MathFormatter()
        self.calc_engine = CalculationEngine()
        self.voice_handler = VoiceHandler(self)
        
        self.create_ui()
        
        self.setup_keyboard_bindings()
    
    def create_ui(self):

        self.create_header()
        
        self.display = DisplayPanel(self.root, self)
        
        self.create_status_bar()
        
        self.create_history_panel()
        
        self.create_voice_button()
        
        self.function_tabs = FunctionTabs(self.root, self)
        
        self.number_pad = NumberPad(self.root, self)
        
        self.menu_bar = MenuBar(self.root, self)
    
    def create_header(self):
        header_frame = tk.Frame(self.root, bg='#1e272e', height=50)
        header_frame.pack(fill='x', padx=15, pady=(15, 5))
        header_frame.pack_propagate(False)
        
        title_frame = tk.Frame(header_frame, bg='#1e272e')
        title_frame.pack(expand=True)
        
        title_font = tkfont.Font(family="Segoe UI", size=16, weight="bold")
        tk.Label(
            title_frame, 
            text="Voice Operated Scientific Calculator", 
            font=title_font, 
            bg='#1e272e', 
            fg='#5f27cd'
        ).pack(side='left')
        
        voice_badge = tk.Label(
            title_frame,
            text=" 🎤 ",
            font=("Segoe UI", 14),
            bg='#ee5a6f',
            fg='white',
            padx=6,
            pady=2
        )
        voice_badge.pack(side='left', padx=(10, 0))
    
    def create_status_bar(self):
        status_frame = tk.Frame(self.root, bg='#1a1a1a', height=30)
        status_frame.pack(fill='x', padx=10, pady=(0, 5))
        status_frame.pack_propagate(False)
        
        left_frame = tk.Frame(status_frame, bg='#1a1a1a')
        left_frame.pack(side='left', fill='y')
        
        self.mode_label = tk.Label(
            left_frame, text=f"[{angle_mode.get_mode()}]",
            font=("Arial", 10, "bold"), bg='#1a1a1a', fg='#00ff00'
        )
        self.mode_label.pack(side='left', padx=5)
        
        self.voice_indicator = tk.Label(
            status_frame, 
            text="🎤" if self.voice_handler.voice_available else "🎤✗",
            font=("Arial", 12), bg='#1a1a1a',
            fg='#00ff00' if self.voice_handler.voice_available else '#666666'
        )
        self.voice_indicator.pack(side='right', padx=5)
    
    def create_history_panel(self):
        history_frame = tk.Frame(self.root, bg='#2a2a2a')
        history_frame.pack(fill='x', padx=10, pady=5)
        
        self.history_btn = tk.Button(
            history_frame, text="▼ History", font=("Arial", 9),
            bg='#3a3a3a', fg='white', command=self.toggle_history
        )
        self.history_btn.pack(fill='x')
        
        self.history_content = tk.Frame(history_frame, bg='#2a2a2a', height=0)
        self.history_visible = False
        
        self.history_text = scrolledtext.ScrolledText(
            self.history_content, height=6, font=("Courier", 9),
            bg='#1a1a1a', fg='#00ff00', state='disabled'
        )
        self.history_text.pack(fill='both', expand=True, padx=5, pady=5)
    
    def create_voice_button(self):
        if not self.voice_handler.voice_available:
            return
            
        voice_frame = tk.Frame(self.root, bg='#2a2a2a')
        voice_frame.pack(fill='x', padx=10, pady=8)
        
        self.voice_btn = tk.Button(
            voice_frame, text="🎤 VOICE INPUT",
            font=("Arial", 12, "bold"), bg='#4a4a4a', fg='white',
            activebackground='#ff4444', height=2, relief='raised', bd=3,
            command=self.voice_handler.toggle_voice_input
        )
        self.voice_btn.pack(fill='x', padx=20)
    
    def setup_keyboard_bindings(self):
        self.root.bind('<Escape>', lambda e: self.handle_button_click('AC'))
        self.root.bind('<Up>', self.history_up)
        self.root.bind('<Down>', self.history_down)
    
    def on_entry_change(self, event=None):
        self.expression = self.display.expression_entry.get()
        formatted = self.formatter.format_expression(self.expression)
        self.display.math_display.config(text=formatted)
    
    def on_backspace(self, event=None):
        self.root.after(10, self.on_entry_change)
    
    def insert_text(self, text):
        pos = self.display.expression_entry.index(tk.INSERT)
        self.display.expression_entry.insert(pos, text)
        self.display.expression_entry.focus_set()
        self.on_entry_change()
    
    def insert_function(self, func):
        self.insert_text(f"{func}(")
    
    def handle_button_click(self, btn_text):
        if btn_text == 'AC':
            self.display.expression_entry.delete(0, tk.END)
            self.display.result_display.config(state='normal')
            self.display.result_display.delete('1.0', tk.END)
            self.display.result_display.insert('1.0', '0')
            self.display.result_display.config(state='disabled')
            self.display.math_display.config(text='')
            return
            
        elif btn_text == 'DEL':
            pos = self.display.expression_entry.index(tk.INSERT)
            if pos > 0:
                self.display.expression_entry.delete(pos-1, pos)
            self.on_entry_change()
            return
            
        elif btn_text == '=':
            self.calculate_result()
            return
            
        elif btn_text == '×':
            self.insert_text('*')
            
        elif btn_text == '÷':
            self.insert_text('/')
        
        elif btn_text == '%':
            self.insert_text('%')
        
        elif btn_text == 'ans':
            self.insert_text('ans')
            
        else:
            self.insert_text(btn_text)
    
    def calculate_result(self):
        try:
            expr = self.display.expression_entry.get()
            result, formatted_result = self.calc_engine.process_and_calculate(
                expr, self.formatter
            )
            
            if result is None:
                return
            
            self.display.result_display.config(state='normal')
            self.display.result_display.delete('1.0', tk.END)
            self.display.result_display.insert('1.0', formatted_result)
            self.display.result_display.config(state='disabled')
            
            self.add_to_history(expr, formatted_result)
            
        except Exception as e:
            self.display.result_display.config(state='normal')
            self.display.result_display.delete('1.0', tk.END)
            self.display.result_display.insert('1.0', f"Error:\n{str(e)[:100]}")
            self.display.result_display.config(state='disabled')
    
    def toggle_history(self):
        if self.history_visible:
            self.history_content.pack_forget()
            self.history_btn.config(text="▼ History")
            self.history_visible = False
        else:
            self.history_content.pack(fill='both', expand=True)
            self.history_btn.config(text="▲ History")
            self.history_visible = True
            self.update_history_display()
    
    def add_to_history(self, expr, result):
        self.history_text.config(state='normal')
        formatted_expr = self.formatter.format_expression(expr)
        self.history_text.insert('1.0', f"{formatted_expr} = {result}\n")
        self.history_text.config(state='disabled')
    
    def update_history_display(self):
        history = history_manager.get_last(20)
        self.history_text.config(state='normal')
        self.history_text.delete('1.0', 'end')
        for entry in reversed(history):
            formatted_expr = self.formatter.format_expression(entry['expression'])
            formatted_result = self.formatter.format_result(entry['result'])
            self.history_text.insert('end', f"{formatted_expr} = {formatted_result}\n")
        self.history_text.config(state='disabled')
    
    def history_up(self, event=None):
        entry = history_manager.navigate_up()
        if entry:
            self.display.expression_entry.delete(0, tk.END)
            self.display.expression_entry.insert(0, entry['expression'])
            self.on_entry_change()
    
    def history_down(self, event=None):
        entry = history_manager.navigate_down()
        if entry:
            self.display.expression_entry.delete(0, tk.END)
            self.display.expression_entry.insert(0, entry['expression'])
            self.on_entry_change()
    
    def clear_history(self):
        history_manager.clear()
        self.history_text.config(state='normal')
        self.history_text.delete('1.0', 'end')
        self.history_text.config(state='disabled')
    
    def set_angle_mode(self, mode):
        angle_mode.set_mode(mode)
        self.mode_label.config(text=f"[{mode}]")
    
    def show_quick_guide(self):
        UIHelpers.show_quick_guide(self.root)
    
    def show_about(self):
        UIHelpers.show_about(self.root)


def run_gui():
    root = tk.Tk()
    app = CasioCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()