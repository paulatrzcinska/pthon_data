import tkinter as tk
import customtkinter
from tkinter import messagebox, simpledialog
from gas_stations_per_kilometer import plot_gas_stations_per_kilometer
from gas_stations_most_popular_company import plot_gas_stations_most_popular_company
from password import plot_password
from population1 import plot_population1
from population2 import plot_population2
from gas_stations_read_data import companies

customtkinter.set_appearance_mode("dark")


# Function to handle population plot 2 with a prompt window
def handle_population2_plot():
    dialog = customtkinter.CTkInputDialog(text="Enter year for Population Plot 2 (data is available for 2013-2050):",
                                          title="Provide data")
    user_input = dialog.get_input()

    if user_input:  # Check if user input is provided
        try:
            plot_population2(user_input)  # Call the plot function with the user input
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid year.")
    else:
        messagebox.showwarning("Warning", "No input provided.")


def handle_gas_stations_most_popular_company_plot():
    # Create a new top-level window for the dropdown selection
    top = customtkinter.CTkToplevel()
    top.title("Select a Company")
    top.geometry("300x150")
    #top.grab_set()

    # Convert dictionary values to a list for the dropdown menu
    company_options = list(companies.values())

    def combobox_callback(choice):
        top.destroy()
        plot_gas_stations_most_popular_company(choice)

    customtkinter.set_appearance_mode("dark")
    dropdown = customtkinter.CTkOptionMenu(master=top, values=company_options, command=combobox_callback)
    dropdown.pack(pady=10)


# Create a new function to initialize the GUI
def initialize_gui():
    # Setting up the main tkinter window
    root = customtkinter.CTk()
    root.title("Data Visualization")
    root.geometry("300x200")

    btn_plot_gas_stations = customtkinter.CTkButton(master=root, text="Show Top 20 Roads Plot",
                                                    command=plot_gas_stations_per_kilometer, width=25)
    btn_plot_gas_stations.pack(pady=5, padx=20, anchor="w")

    btn_plot_gas_stations_most_popular_company = customtkinter.CTkButton(master=root,
                                                                         text="Show Roads Per Company Plot",
                                                                         command=handle_gas_stations_most_popular_company_plot,
                                                                         width=25)
    btn_plot_gas_stations_most_popular_company.pack(pady=5, padx=20, anchor="w")

    btn_plot_password = customtkinter.CTkButton(master=root, text="Show Passwords Plot", command=plot_password,
                                                width=25)
    btn_plot_password.pack(pady=5, padx=20, anchor="w")

    btn_plot_population1 = customtkinter.CTkButton(master=root, text="Show Population Plot 1", command=plot_population1,
                                                   width=25)
    btn_plot_population1.pack(pady=5, padx=20, anchor="w")

    btn_plot_population2 = customtkinter.CTkButton(master=root, text="Show Population Plot 2",
                                                   command=handle_population2_plot, width=25)
    btn_plot_population2.pack(pady=5, padx=20, anchor="w")

    root.mainloop()


if __name__ == "__main__":
    initialize_gui()
