# dashboard.py content goes here
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def open_dashboard():
    win = tk.Toplevel()
    win.title("Dashboard - Top Selling Products")
    win.geometry("700x500")

    # Sample dummy sales data
    products = ["Milk", "Bread", "Butter", "Eggs", "Juice"]
    quantities = [120, 95, 78, 65, 40]

    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(products, quantities, color="skyblue")
    ax.set_title("Top Selling Products")
    ax.set_xlabel("Product")
    ax.set_ylabel("Quantity Sold")

    # Annotate bar values
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 2, str(height), ha='center', va='bottom')

    # Embed plot in Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both', padx=10, pady=10)
