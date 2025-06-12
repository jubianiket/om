# purchase.py content goes here
import tkinter as tk
import sqlite3
from tkinter import messagebox

def open_purchase():
    win = tk.Toplevel()
    win.title("Purchase Entry")
    win.geometry("400x300")
    
    # Define input variables
    name_var = tk.StringVar()
    qty_var = tk.StringVar()
    rate_var = tk.StringVar()

    # Input fields
    tk.Label(win, text="Product Name").pack(pady=5)
    tk.Entry(win, textvariable=name_var).pack()

    tk.Label(win, text="Quantity").pack(pady=5)
    tk.Entry(win, textvariable=qty_var).pack()

    tk.Label(win, text="Rate per Unit").pack(pady=5)
    tk.Entry(win, textvariable=rate_var).pack()

    def add_stock():
        name = name_var.get().strip()
        try:
            qty = int(qty_var.get())
            rate = float(rate_var.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter valid quantity and rate.")
            return

        if not name:
            messagebox.showerror("Missing Name", "Enter product name.")
            return

        try:
            conn = sqlite3.connect("../db/store.db")
            cur = conn.cursor()

            # Check if product exists
            cur.execute("SELECT id FROM products WHERE name = ?", (name,))
            row = cur.fetchone()

            if row:
                # Update existing product rate (optional)
                cur.execute("UPDATE products SET rate = ? WHERE id = ?", (rate, row[0]))
            else:
                # Insert new product
                cur.execute("INSERT INTO products (name, rate) VALUES (?, ?)", (name, rate))
            conn.commit()
            conn.close()

            messagebox.showinfo("Stock Added", f"{qty} units of {name} added at ₹{rate} per unit.")
            name_var.set("")
            qty_var.set("")
            rate_var.set("")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    tk.Button(win, text="Add to Stock", command=add_stock).pack(pady=20)
