import tkinter as tk


class NumberPad:
    
    def __init__(self, parent_frame, parent):
        self.parent = parent
        self.numpad_frame = tk.Frame(parent_frame, bg='#2a2a2a')
        self.numpad_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        self.create_buttons()
    
    def create_buttons(self):
        """Create modern styled number pad buttons"""
        buttons = [
            ['7', '8', '9', 'DEL', 'AC'],
            ['4', '5', '6', '×', '÷'],
            ['1', '2', '3', '+', '-'],
            ['0', '.', '%', '(', ')'],
            ['ans', '=']  
        ]
        
        for row_idx, row in enumerate(buttons):
            row_frame = tk.Frame(self.numpad_frame, bg='#2a2a2a')
            row_frame.pack(fill='both', expand=True, pady=3)
            
            if row_idx == 4:
                bg_color, fg_color, hover_color = self._get_button_colors('ans')
                ans_btn = self._create_modern_button(
                    row_frame, 'ans', bg_color, fg_color, hover_color,
                    width=1, height=2, font_size=14
                )
                ans_btn.pack(side='left', padx=3, expand=False, fill='both')
                ans_btn.pack_configure(side='left', expand=True, fill='both')
                
                bg_color, fg_color, hover_color = self._get_button_colors('=')
                eq_btn = self._create_modern_button(
                    row_frame, '=', bg_color, fg_color, hover_color,
                    width=1, height=2, font_size=18
                )
                eq_btn.pack(side='left', padx=3, expand=True, fill='both')
                eq_btn.pack_configure(side='left', expand=True, fill='both')
            else:
                for btn_text in row:
                    bg_color, fg_color, hover_color = self._get_button_colors(btn_text)
                    
                    btn = self._create_modern_button(
                        row_frame, btn_text, bg_color, fg_color, hover_color,
                        width=1, height=2, font_size=16
                    )
                    btn.pack(side='left', padx=3, expand=True, fill='both')
    
    def _create_modern_button(self, parent, text, bg, fg, hover_bg, width, height, font_size):
        btn = tk.Button(
            parent, text=text,
            font=("Segoe UI", font_size, "bold"),
            bg=bg, fg=fg,
            activebackground=hover_bg,
            activeforeground=fg,
            width=width, height=height,
            relief='flat',
            bd=0,
            cursor='hand2',
            command=lambda: self.parent.handle_button_click(text)
        )
        
        btn.bind('<Enter>', lambda e: btn.config(bg=hover_bg))
        btn.bind('<Leave>', lambda e: btn.config(bg=bg))
        
        return btn
    
    def _get_button_colors(self, btn_text):
        if btn_text in ['AC', 'DEL']:
            return '#ff4757', 'white', '#ff6b81'  # Red
        elif btn_text == '=':
            return '#5f27cd', 'white', '#341f97'  # Purple
        elif btn_text == 'ans':
            return '#ee5a6f', 'white', '#ff6348'  # Pink/Orange
        elif btn_text in ['×', '÷', '+', '-']:
            return '#54a0ff', 'white', '#2e86de'  # Blue
        elif btn_text in ['(', ')']:
            return '#48dbfb', '#222f3e', '#0abde3'  # Cyan
        elif btn_text == '%':
            return '#feca57', '#222f3e', '#ff9ff3'  # Yellow
        else:
            return '#f1f2f6', '#2f3640', '#dfe4ea'  # Light gray