import tkinter as tk
from tkinter import messagebox
import serial
import serial.tools.list_ports
import threading
import time

# --- Configuration ---
BAUD_RATE = 9600
uno_serial = None
mega_serial = None

def find_arduinos():
    """Finds and connects to both Uno and Mega boards based on their port description."""
    global uno_serial, mega_serial
    ports = serial.tools.list_ports.comports()
    uno_port, mega_port = None, None

    for p in ports:
        # A robust way to identify Arduinos is by their USB description
        if 'Arduino Uno' in p.description:
            uno_port = p.device
        if 'Arduino Mega' in p.description:
            mega_port = p.device

    # Connect to Arduino Uno
    if uno_port:
        try:
            uno_serial = serial.Serial(uno_port, BAUD_RATE, timeout=1)
            uno_status_label.config(text=f"Uno: Connected on {uno_port}", fg="green")
        except serial.SerialException as e:
            uno_status_label.config(text=f"Uno: Failed ({e})", fg="red")
    else:
        uno_status_label.config(text="Uno: Not found.", fg="red")

    # Connect to Arduino Mega and start a thread to read data
    if mega_port:
        try:
            mega_serial = serial.Serial(mega_port, BAUD_RATE, timeout=1)
            mega_status_label.config(text=f"Mega: Connected on {mega_port}", fg="green")
            # Start a separate thread for continuous reading from the Mega
            threading.Thread(target=read_from_mega, daemon=True).start()
        except serial.SerialException as e:
            mega_status_label.config(text=f"Mega: Failed ({e})", fg="red")
    else:
        mega_status_label.config(text="Mega: Not found.", fg="red")

def read_from_mega():
    """Reads data from the Mega and updates the GUI periodically."""
    while mega_serial and mega_serial.is_open:
        try:
            if mega_serial.in_waiting > 0:
                data = mega_serial.readline().decode('utf-8').strip()
                if data:
                    # For debugging
                    print(f"Mega: {data}")
                    
                    # Update GUI based on received data format
                    if data.startswith("Distance:"):
                        distance_label.config(text=data)
                    elif "ALERT" in data:
                        alert_label.config(text=data, fg="red")
                    elif "System" in data:
                        system_label.config(text=data)
        except serial.SerialException:
            mega_status_label.config(text="Mega: Disconnected.", fg="red")
            break
        time.sleep(0.1)

def send_command(device, command):
    """Sends a command to the specified Arduino."""
    if device == 'uno' and uno_serial and uno_serial.is_open:
        try:
            uno_serial.write(command.encode('utf-8'))
            print(f"Uno Sent: {command.strip()}")
        except serial.SerialException:
            uno_status_label.config(text="Uno: Connection lost.", fg="red")
    elif device == 'mega' and mega_serial and mega_serial.is_open:
        try:
            mega_serial.write(command.encode('utf-8'))
            print(f"Mega Sent: {command.strip()}")
        except serial.SerialException:
            mega_status_label.config(text="Mega: Connection lost.", fg="red")
    else:
        messagebox.showerror("Error", "Not connected to the specified Arduino.")

# --- GUI setup ---
root = tk.Tk()
root.title("IoT Vehicle Controller")
root.geometry("500x450")

# Connection frame
conn_frame = tk.Frame(root)
conn_frame.pack(pady=10)
connect_button = tk.Button(conn_frame, text="Connect Arduinos", command=find_arduinos)
connect_button.pack(side=tk.LEFT, padx=10)
uno_status_label = tk.Label(conn_frame, text="Uno: Disconnected", fg="gray")
uno_status_label.pack(side=tk.LEFT)
mega_status_label = tk.Label(conn_frame, text="Mega: Disconnected", fg="gray")
mega_status_label.pack(side=tk.LEFT, padx=10)

# Vehicle control frame
vehicle_frame = tk.LabelFrame(root, text="Vehicle Controls")
vehicle_frame.pack(pady=10)
tk.Button(vehicle_frame, text="Forward", command=lambda: send_command('uno', "FORWARD\n")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(vehicle_frame, text="Left", command=lambda: send_command('uno', "LEFT\n")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(vehicle_frame, text="Stop", command=lambda: send_command('uno', "STOP\n")).grid(row=1, column=1, padx=5, pady=5)
tk.Button(vehicle_frame, text="Right", command=lambda: send_command('uno', "RIGHT\n")).grid(row=1, column=2, padx=5, pady=5)
tk.Button(vehicle_frame, text="Backward", command=lambda: send_command('uno', "BACKWARD\n")).grid(row=2, column=1, padx=5, pady=5)

# Status monitoring frame
status_frame = tk.LabelFrame(root, text="Status & Alerts")
status_frame.pack(pady=10)
distance_label = tk.Label(status_frame, text="Distance: N/A", font=("Arial", 12))
distance_label.pack(pady=5)
alert_label = tk.Label(status_frame, text="System Normal", font=("Arial", 14, "bold"))
alert_label.pack(pady=5)
system_label = tk.Label(status_frame, text="System: Disarmed", font=("Arial", 12))
system_label.pack(pady=5)

# Anti-theft control frame
system_control_frame = tk.LabelFrame(root, text="System Control")
system_control_frame.pack(pady=10)
tk.Button(system_control_frame, text="Arm System", command=lambda: send_command('mega', "ARM\n")).pack(side=tk.LEFT, padx=10)
tk.Button(system_control_frame, text="Disarm System", command=lambda: send_command('mega', "DISARM\n")).pack(side=tk.LEFT, padx=10)

# Start the main event loop
root.mainloop()
