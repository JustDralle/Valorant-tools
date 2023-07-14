import tkinter as tk
from tkinter import ttk

class AgentsInfoTab(tk.Frame):
    def __init__(self, tab_control):
        super().__init__(tab_control)
        
        # Create and add the agents info tab
        tab_control.add(self, text='Agents Info')
        
        # Add content to the agents info tab with AMOLED theme
        self.configure(background='#000000')  # Set background color to black
        label = ttk.Label(self, text="Here you'll find information about agents.", font=('Arial', 16), background='#000000', foreground='#FFFFFF')
        label.pack(pady=20)
