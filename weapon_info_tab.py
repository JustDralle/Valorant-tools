import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import io

class WeaponInfoTab(tk.Frame):
    def __init__(self, tab_control):
        super().__init__(tab_control)
        
        # Create and add the weapon info tab
        tab_control.add(self, text='Weapon Info')
        
        # Create a style for the content frame
        style = ttk.Style()
        style.configure('Content.TFrame', background='#000000')
        
        # Create a canvas widget
        canvas = tk.Canvas(self, bg="#000000", highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create a scrollbar widget
        scrollbar_style = ttk.Style()
        scrollbar_style.configure("CustomScrollbar.Vertical.TScrollbar", gripcount=0,
                                  background="#666666", darkcolor="#666666", lightcolor="#666666",
                                  troughcolor="#000000", bordercolor="#000000", arrowcolor="#FFFFFF")
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview, style="CustomScrollbar.Vertical.TScrollbar")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create a frame inside the canvas to hold the content
        content_frame = ttk.Frame(canvas, style='Content.TFrame')
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add the content frame to the canvas
        canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)
        
        # Function to update canvas scrolling region
        def update_canvas_scroll_region():
            canvas.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox(tk.ALL))
        
        # Create a label for the dropdown selection
        weapon_label = ttk.Label(content_frame, text="Select a weapon:", font=('Arial', 12), background='#000000', foreground='#FFFFFF')
        weapon_label.pack(pady=10)
        
        # Create a dropdown list for weapon selection
        weapon_selection = ttk.Combobox(content_frame, state='readonly', font=('Arial', 12))
        weapon_selection['values'] = ('Vandal', 'Spectre', 'Phantom')  # Replace with actual weapon names
        weapon_selection.current(0)  # Set the default selection
        weapon_selection.pack(pady=5)
        
        # Create a label to display weapon information
        weapon_info_label = ttk.Label(content_frame, text="", font=('Arial', 12), background='#000000', foreground='#FFFFFF')
        weapon_info_label.pack(pady=10)
        
        # Create a label to display weapon image
        weapon_image_label = ttk.Label(content_frame, background='#000000')
        weapon_image_label.pack(pady=10)
        
        # Dictionary mapping weapon names to image URLs
        weapon_images = {
            'Vandal': 'https://static.wikia.nocookie.net/valorant/images/5/56/Vandal.png',
            'Spectre': 'https://static.wikia.nocookie.net/valorant/images/9/90/Spectre.png',
            'Phantom': 'https://static.wikia.nocookie.net/valorant/images/e/ec/Phantom.png',
        }
        
        # Function to update weapon information and image based on selection
        def update_weapon_info():
            selected_weapon = weapon_selection.get()
            
            # Update the weapon information label
            weapon_info_label.configure(text=f"Weapon: {selected_weapon} Info")
            
            # Fetch the weapon image from the URL
            image_url = weapon_images[selected_weapon]
            response = requests.get(image_url)
            image_data = response.content
            
            # Create an image from the fetched data
            image = Image.open(io.BytesIO(image_data))
            weapon_image = ImageTk.PhotoImage(image)
            
            # Update the weapon image label
            weapon_image_label.configure(image=weapon_image)
            weapon_image_label.image = weapon_image  # Store a reference to prevent garbage collection
            
            # Additional information for the Phantom weapon
            if selected_weapon == 'Phantom':
                weapon_info = """
                Type: Rifle
                Creds: 2,900
                Wall Penetration: Medium
                Features: Silenced, Tracers not visible to enemies, Firing sound can't be heard at 40m+ except in direction of fire
                Killfeed Icon: Phantom killfeed
                Length: 121.11 cm (90.59 cm without silencer)
                Creator: Bulwark Armory
                Primary Fire: Auto
                Fire Rate: 11 rounds/sec (660 RPM)
                Run Speed: 5.4 m/sec
                Equip Speed: 1 sec
                Reload Speed: 2.5 sec
                Magazine: 30
                Reserve: 60 (2 magazines)
                
                Damage:
                0 - 15m: Head - 156, Body - 39, Leg - 33
                15 - 30m: Head - 140, Body - 35, Leg - 29
                30 - 50m: Head - 124, Body - 31, Leg - 26
                
                Alt Fire:
                Function: Aim down sights
                Zoom: 1.25x
                Fire Rate: 90% (9.9 rounds/sec, 594 RPM)
                Move Speed: 76% (4.104 m/sec)
                Note: Slight spread and recoil reduction
                """
                weapon_info_label.configure(text=weapon_info)
                
                # Update the canvas scrolling region after updating the content
                update_canvas_scroll_region()
        
        # Bind the dropdown selection event to the update function
        weapon_selection.bind("<<ComboboxSelected>>", lambda event: update_weapon_info())
        
        # Initial update to display the default weapon information
        update_weapon_info()
        
        # Bind the canvas scrolling to the mouse wheel event
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
