import tkinter as tk
from tkinter import ttk
import subprocess
import threading

class StreamerYoinkerTab(tk.Frame):
    def __init__(self, tab_control):
        super().__init__(tab_control)
        tab_control.add(self, text='Agents Instalocker')

        # Create a text widget to display the output
        output_text = tk.Text(self, height=10, width=50)
        output_text.pack(pady=20)

        # Function to execute the Valorant Stream Yoinker script
        def execute_valorant_stream_yoinker():
            # Clear the text widget before executing the script
            output_text.delete(1.0, tk.END)

            # Read the contents of the settings.json file
            with open('C:\\Users\\dehod\\Desktop\\Valorant-tools\\agentYoinker\\settings.json', 'r') as f:
                contents = f.read()
                print(contents)

            # Execute the Valorant Stream Yoinker script in a separate thread
            def run_script():
                try:
                    subprocess.run(['python', 'C:\\Users\\dehod\\Desktop\\Valorant-tools\\agentYoinker\\main.py'],
                                   capture_output=True, text=True, check=True, shell=True)
                except subprocess.CalledProcessError as e:
                    output_text.insert(tk.END, f"An error occurred: {e.stderr}")
                except Exception as e:
                    output_text.insert(tk.END, f"An error occurred: {str(e)}")

            # Create a new thread and run the script
            thread = threading.Thread(target=run_script)
            thread.start()

        # Create a button to execute the Valorant Stream Yoinker script
        execute_button = ttk.Button(self, text="Execute Valorant Stream Yoinker", command=execute_valorant_stream_yoinker)
        execute_button.pack(pady=10)

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

# Add the Agents Instalocker tab
agents_instalocker_tab = StreamerYoinkerTab(tab_control)

# Start the GUI main loop
window.mainloop()
