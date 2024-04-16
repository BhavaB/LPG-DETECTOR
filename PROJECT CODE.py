import tkinter as tk
from tkinter import messagebox
import winsound

# Define gas thresholds
LPG_THRESHOLD = 0.5  # Threshold for LPG detection
GASOLINE_THRESHOLD = 0.3  # Threshold for gasoline detection

def detect_gas(lpg_level, gasoline_level):
    lpg_detected = lpg_level > LPG_THRESHOLD
    gasoline_detected = gasoline_level > GASOLINE_THRESHOLD

    lpg_status.config(text="LPG Detected!" if lpg_detected else "No LPG Detected", fg="red" if lpg_detected else "black")
    gasoline_status.config(text="Gasoline Detected!" if gasoline_detected else "No Gasoline Detected", fg="red" if gasoline_detected else "black")

    if lpg_detected or gasoline_detected:
        winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 milliseconds
        messagebox.showwarning("Gas Detected", "Gas detected! Take necessary precautions.")

# Function to update gas levels
def update_gas_levels():
    lpg_level = lpg_slider.get()
    gasoline_level = gasoline_slider.get()
    detect_gas(lpg_level, gasoline_level)

# Create Tkinter window
root = tk.Tk()
root.title("LPG and Gasoline Detection System")

# LPG Detection Section
lpg_frame = tk.Frame(root)
lpg_frame.pack(pady=10)

lpg_label = tk.Label(lpg_frame, text="LPG Level:")
lpg_label.grid(row=0, column=0)

lpg_slider = tk.Scale(lpg_frame, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL)
lpg_slider.grid(row=0, column=1)

# Gasoline Detection Section
gasoline_frame = tk.Frame(root)
gasoline_frame.pack(pady=10)

gasoline_label = tk.Label(gasoline_frame, text="Gasoline Level:")
gasoline_label.grid(row=0, column=0)

gasoline_slider = tk.Scale(gasoline_frame, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL)
gasoline_slider.grid(row=0, column=1)

# Status Display Section
status_frame = tk.Frame(root)
status_frame.pack(pady=10)

lpg_status = tk.Label(status_frame, text="No LPG Detected", fg="black")
lpg_status.grid(row=0, column=0, padx=10)

gasoline_status = tk.Label(status_frame, text="No Gasoline Detected", fg="black")
gasoline_status.grid(row=0, column=1, padx=10)

# Update Button
update_button = tk.Button(root, text="Update", command=update_gas_levels)
update_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
