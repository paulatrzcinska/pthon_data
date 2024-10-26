import tkinter as tk
from tkinter import messagebox
from gas_stations_per_kilometer import plot_gas_stations_per_kilometer
from password import plot_password
from population1 import plot_population1
from population2 import  plot_population2


# Function to show an informational message for unimplemented plots
def show_other_plot():
    messagebox.showinfo("Info", "Functionality for this plot is not yet implemented.")


# Create a new function to initialize the GUI
def initialize_gui():
    # Setting up the main tkinter window
    root = tk.Tk()
    root.title("Data Visualization")
    root.geometry("400x300")  # Set a larger window size for better display

    # Adding buttons for each plot type
    btn_plot_top_20_roads = tk.Button(root, text="Show Top 20 Roads Plot", command=plot_gas_stations_per_kilometer)
    btn_plot_top_20_roads.pack(pady=10, padx=20, anchor="w", side="top")

    btn_plot_top_20_roads = tk.Button(root, text="Show Passwords Plot", command=plot_password)
    btn_plot_top_20_roads.pack(pady=10, padx=20, anchor="w", side="top")

    btn_plot_top_20_roads = tk.Button(root, text="Show Population Plot 1", command=plot_population1)
    btn_plot_top_20_roads.pack(pady=10, padx=20, anchor="w", side="top")

    btn_plot_top_20_roads = tk.Button(root, text="Show Population Plot 2", command=plot_population2)
    btn_plot_top_20_roads.pack(pady=10, padx=20, anchor="w", side="top")

    root.mainloop()


# Run the GUI
if __name__ == "__main__":
    initialize_gui()
