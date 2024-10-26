import tkinter as tk
from tkinter import messagebox, simpledialog
from gas_stations_per_kilometer import plot_gas_stations_per_kilometer
from password import plot_password
from population1 import plot_population1
from population2 import plot_population2


# Function to handle population plot 2 with a prompt window
def handle_population2_plot():
    user_input = simpledialog.askstring("Input", "Enter year for Population Plot 2 (data is available for 2013-2050):")
    if user_input:  # Check if user input is provided
        try:
            plot_population2(user_input)  # Call the plot function with the user input
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid year.")
    else:
        messagebox.showwarning("Warning", "No input provided.")


# Create a new function to initialize the GUI
def initialize_gui():
    # Setting up the main tkinter window
    root = tk.Tk()
    root.title("Data Visualization")
    root.geometry("500x300")  # Set a larger window size for better display

    # Adding buttons for each plot type
    btn_plot_gas_stations = tk.Button(root, text="Show Top 20 Roads Plot", command=plot_gas_stations_per_kilometer)
    btn_plot_gas_stations.pack(pady=10, padx=20, anchor="w", side="top")

    btn_plot_password = tk.Button(root, text="Show Passwords Plot", command=plot_password)
    btn_plot_password.pack(pady=10, padx=20, anchor="w", side="top")

    btn_plot_population1 = tk.Button(root, text="Show Population Plot 1", command=plot_population1)
    btn_plot_population1.pack(pady=10, padx=20, anchor="w", side="top")

    # Button for Population Plot 2 with prompt input via dialog
    btn_plot_population2 = tk.Button(root, text="Show Population Plot 2", command=handle_population2_plot)
    btn_plot_population2.pack(pady=10, padx=20, anchor="w", side="top")

    root.mainloop()


# Run the GUI
if __name__ == "__main__":
    initialize_gui()
