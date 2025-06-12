# purchase.py
import tkinter as tk
import sqlite3
from tkinter import messagebox

def open_purchase(main_frame):
    # Clear the frame first
    for widget in main_frame.winfo_children():
        widget.destroy()

    # --- Heading ---
    tk.Label(main_frame, text="📥 Purchase Entry", font=("Arial", 16, "bold"), fg="darkblue").pack(pady=10)

    # --- Input Variables ---
    name_var = tk.StringVar()
    qty_var = tk.StringVar()
    rate_var = tk.StringVar()

    # --- Form Fields ---
    tk.Label(main_frame, text="Product Name").pack(anchor="w", padx=10)
    tk.Entry(main_frame, textvariable=name_var, width=30).pack(padx=10, pady=2)

    tk.Label(main_frame, text="Quantity").pack(anchor="w", padx=10)
    tk.Entry(main_frame, textvariable=qty_var, width=30).pack(padx=10, pady=2)

    tk.Label(main_frame, text="Rate per Unit").pack(anchor="w", padx=10)
    tk.Entry(main_frame, textvariable=rate_var, width=30).pack(padx=10, pady=2)

    # --- Add to Stock Handler ---
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
            conn = sqlite3.connect("db/store.db")
            cur = conn.cursor()

            # Check if product exists
            cur.execute("SELECT id FROM products WHERE name = ?", (name,))
            row = cur.fetchone()

            if row:
                # Update rate
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

    # --- Submit Button ---
    tk.Button(main_frame, text="➕ Add to Stock", command=add_stock, bg="green", fg="white").pack(pady=20)
