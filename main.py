import tkinter as tk
from tkinter import ttk
from home_tab import HomeTab
from weapon_info_tab import WeaponInfoTab
from agents_info_tab import AgentsInfoTab
from agents_instalocker_tab import StreamerYoinkerTab
from aNOTnymous import aNOTnymoustab

# Create the main window
window = tk.Tk()
window.title("Tool Selection")
window.geometry("800x600")
window.configure(bg="#000000")  # Set background color to black

# Create a style for the AMOLED theme
style = ttk.Style()
style.theme_use('clam')

# Configure the style for the AMOLED theme
style.configure('TNotebook',
                background='#000000',
                foreground='#FFFFFF',
                bordercolor='#000000',
                borderwidth=2)  # Set border color to black and border width to 2

# Create a notebook widget
tab_control = ttk.Notebook(window)
tab_control.pack(fill='both', expand=True)

# Create the tabs
home_tab = HomeTab(tab_control)
weapon_info_tab = WeaponInfoTab(tab_control)
agents_info_tab = AgentsInfoTab(tab_control)
agents_instalocker_tab = StreamerYoinkerTab(tab_control)
aNOTnymous_tab = aNOTnymoustab(tab_control)

# Add the tabs to the notebook
tab_control.add(home_tab, text="Home")
tab_control.add(weapon_info_tab, text="Weapon Info")
tab_control.add(agents_info_tab, text="Agents Info")
tab_control.add(agents_instalocker_tab, text="Agents Instalocker")
tab_control.add(aNOTnymous_tab, text="aNOTnymous")

# Start the GUI main loop
window.mainloop()
