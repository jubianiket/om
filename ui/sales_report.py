# sales_report.py content goes here
import tkinter as tk
from tkinter import ttk
import sqlite3

def open_sales_report():
    win = tk.Toplevel()
    win.title("Sales Report")
    win.geometry("600x400")

    cols = ("ID", "Item", "Qty", "Amount")
    tree = ttk.Treeview(win, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)
    tree.pack(expand=True, fill='both', padx=10, pady=10)

    # In real version, load from 'sales' table
    dummy_data = [
        (1, "Milk", 2, 50),
        (2, "Bread", 3, 60),
        (3, "Butter", 1, 45),
        (4, "Eggs", 2, 120)
    ]

    for row in dummy_data:
        tree.insert("", "end", values=row)
