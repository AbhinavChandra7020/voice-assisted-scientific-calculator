
import tkinter as tk
from tkinter import scrolledtext


def apply_modern_window_style(window, title, width, height):
    window.title(title)
    window.geometry(f"{width}x{height}")
    window.configure(bg='#2a2a2a')
    window.resizable(False, False)
    
    # Add border effect
    border_frame = tk.Frame(
        window,
        bg='#5f27cd',
        highlightthickness=0
    )
    border_frame.pack(fill='both', expand=True, padx=2, pady=2)
    
    content_frame = tk.Frame(border_frame, bg='#2a2a2a')
    content_frame.pack(fill='both', expand=True, padx=1, pady=1)
    
    return content_frame


class UIHelpers:
    
    @staticmethod
    def show_quick_guide(root):
        guide_window = tk.Toplevel(root)
        content = apply_modern_window_style(guide_window, "Quick Guide", 680, 600)
        
        title_label = tk.Label(
            content,
            text="📖 Quick Reference Guide",
            font=("Segoe UI", 18, "bold"),
            bg='#2a2a2a',
            fg='#5f27cd',
            pady=15
        )
        title_label.pack()
        
        text_frame = tk.Frame(content, bg='#2a2a2a')
        text_frame.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        
        text = scrolledtext.ScrolledText(
            text_frame,
            wrap='word',
            font=("Consolas", 10),
            bg='#1e272e',
            fg='#f1f2f6',
            insertbackground='#5f27cd',
            relief='flat',
            bd=0,
            padx=15,
            pady=15
        )
        text.pack(fill='both', expand=True)
        
        guide_text = """QUICK GUIDE - Casio fx-991EX Voice

✨ DISPLAY FEATURES:
  • Top: Mathematical notation (√, ∫, π, ², %)
  • Middle: Editable expression with cursor
  • Bottom: Result (formatted beautifully)

⌨️ KEYBOARD SHORTCUTS:
  • Enter: Calculate (=)
  • Backspace: Delete character
  • Escape: Clear (AC)
  • ↑/↓: Navigate history

🎯 PERCENTAGE OPERATIONS:
  percent(50) → 0.5
  percent_add(100, 10) → 110
  percent_sub(100, 10) → 90

🎤 VOICE INPUT:
  • Click VOICE button
  • Speak clearly
  • Auto-calculate

📊 STATISTICS:
  mean([1,2,3,4,5])
  stdev([1,2,3,4,5])

🔢 MATRICES:
  det([[1,2],[3,4]])
  inv([[1,2],[3,4]])

🌡️ CONVERSIONS:
  convert_temp(100, 'c', 'f')
  c_to_f(37)
"""
        text.insert('1.0', guide_text)
        text.config(state='disabled')
    
    @staticmethod
    def show_about(root):
        about_window = tk.Toplevel(root)
        content = apply_modern_window_style(about_window, "About", 500, 450)
        
        title_label = tk.Label(
            content,
            text="🧮",
            font=("Segoe UI", 48),
            bg='#2a2a2a',
            fg='#5f27cd'
        )
        title_label.pack(pady=(30, 10))
        
        tk.Label(
            content,
            text="Casio fx-991EX Voice",
            font=("Segoe UI", 20, "bold"),
            bg='#2a2a2a',
            fg='white'
        ).pack(pady=5)
        
        tk.Label(
            content,
            text="Scientific Calculator with AI Voice Input",
            font=("Segoe UI", 11),
            bg='#2a2a2a',
            fg='#dfe4ea'
        ).pack(pady=5)
        
        tk.Label(
            content,
            text="Version 1.0.0",
            font=("Segoe UI", 9),
            bg='#2a2a2a',
            fg='#747d8c'
        ).pack(pady=15)
        
        features_frame = tk.Frame(
            content,
            bg='#1e272e',
            highlightthickness=1,
            highlightbackground='#5f27cd'
        )
        features_frame.pack(fill='both', expand=True, padx=40, pady=20)
        
        features_text = """
✓ 552+ Mathematical Functions
✓ AI-Powered Voice Input
✓ Beautiful Math Notation
✓ Real-time Calculation
✓ Matrix & Vector Operations
✓ Advanced Statistics
✓ Unit Conversions
✓ History Navigation
"""
        
        tk.Label(
            features_frame,
            text=features_text,
            font=("Segoe UI", 10),
            bg='#1e272e',
            fg='#00d2d3',
            justify='left',
            padx=20,
            pady=20
        ).pack()