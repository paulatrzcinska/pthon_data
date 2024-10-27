import tkinter as tk
from tkinter import messagebox, simpledialog
from gas_stations_per_kilometer import plot_gas_stations_per_kilometer
from gas_stations_most_popular_company import plot_gas_stations_most_popular_company
from password import plot_password
from population1 import plot_population1
from population2 import plot_population2
from gas_stations_read_data import companies


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

def handle_gas_stations_most_popular_company_plot():
    # Create a new top-level window for the dropdown selection
    top = tk.Toplevel()
    top.title("Select a Company")
    top.geometry("300x150")

    # Convert dictionary values to a list for the dropdown menu
    company_options = list(companies.values())
    selected_company = tk.StringVar(top)
    selected_company.set(company_options[0])  # Set default selection

    # Create and pack the dropdown menu
    dropdown = tk.OptionMenu(top, selected_company, *company_options)
    dropdown.pack(pady=10)

    # Function to call the plot function with the selected company
    def confirm_selection():
        top.destroy()  # Close the dropdown window
        plot_gas_stations_most_popular_company(selected_company.get())

    # Button to confirm selection and generate the plot
    confirm_button = tk.Button(top, text="Generate Plot", command=confirm_selection)
    confirm_button.pack(pady=10)


# Create a new function to initialize the GUI
def initialize_gui():
    # Setting up the main tkinter window
    root = tk.Tk()
    root.title("Data Visualization")
    root.geometry("500x300")

    button_width = 25

    btn_plot_gas_stations = tk.Button(root, text="Show Top 20 Roads Plot", command=plot_gas_stations_per_kilometer, width=button_width)
    btn_plot_gas_stations.pack(pady=10, padx=20, anchor="w")

    btn_plot_gas_stations_most_popular_company = tk.Button(root, text="Show Roads Per Company Plot", command=handle_gas_stations_most_popular_company_plot, width=button_width)
    btn_plot_gas_stations_most_popular_company.pack(pady=10, padx=20, anchor="w")

    btn_plot_password = tk.Button(root, text="Show Passwords Plot", command=plot_password, width=button_width)
    btn_plot_password.pack(pady=10, padx=20, anchor="w")

    btn_plot_population1 = tk.Button(root, text="Show Population Plot 1", command=plot_population1, width=button_width)
    btn_plot_population1.pack(pady=10, padx=20, anchor="w")

    btn_plot_population2 = tk.Button(root, text="Show Population Plot 2", command=handle_population2_plot, width=button_width)
    btn_plot_population2.pack(pady=10, padx=20, anchor="w")

    root.mainloop()


if __name__ == "__main__":
    initialize_gui()
