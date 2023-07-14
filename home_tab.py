import tkinter as tk
from tkinter import ttk

class HomeTab(tk.Frame):
    def __init__(self, tab_control):
        super().__init__(tab_control)
        
        # Create and add the home tab
        tab_control.add(self, text='Home')
        
        # Add content to the home tab with AMOLED theme
        self.configure(background='#000000')  # Set background color to black
        label = ttk.Label(self, text="Welcome to the Home tab!", font=('Arial', 16), background='#000000', foreground='#FFFFFF')
        label.pack(pady=20)
