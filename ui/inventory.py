# inventory.py content goes here
import tkinter as tk
import sqlite3
from tkinter import messagebox

def open_inventory():
    win = tk.Toplevel()
    win.title("Inventory Manager")
    win.geometry("400x400")

    def add_product():
        name = name_var.get()
        rate = float(rate_var.get())
        code = code_var.get()
        currency = currency_var.get()

        conn = sqlite3.connect("../db/store.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO products (name, rate, code, currency) VALUES (?, ?, ?, ?)", 
                    (name, rate, code, currency))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Product '{name}' added.")

    name_var = tk.StringVar()
    rate_var = tk.StringVar()
    code_var = tk.StringVar()
    currency_var = tk.StringVar(value="INR")

    tk.Label(win, text="Product Name").pack()
    tk.Entry(win, textvariable=name_var).pack()

    tk.Label(win, text="Rate").pack()
    tk.Entry(win, textvariable=rate_var).pack()

    tk.Label(win, text="Code").pack()
    tk.Entry(win, textvariable=code_var).pack()

    tk.Label(win, text="Currency").pack()
    tk.Entry(win, textvariable=currency_var).pack()

    tk.Button(win, text="Add Product", command=add_product).pack(pady=10)
