# inventory.py
import tkinter as tk
from tkinter import messagebox
import sqlite3

def open_inventory(main_frame):
    # Clear anything inside the main_frame (precautionary, though already handled in main.py)
    for widget in main_frame.winfo_children():
        widget.destroy()

    # --- UI Heading ---
    tk.Label(main_frame, text="📦 Inventory Manager", font=("Arial", 16, "bold"), fg="green").pack(pady=10)

    # --- Variables ---
    name_var = tk.StringVar()
    rate_var = tk.StringVar()
    code_var = tk.StringVar()
    currency_var = tk.StringVar(value="INR")

    # --- Form Fields ---
    tk.Label(main_frame, text="Product Name:").pack(anchor="w", padx=10)
    tk.Entry(main_frame, textvariable=name_var, width=30).pack(padx=10, pady=2)

    tk.Label(main_frame, text="Rate:").pack(anchor="w", padx=10)
    tk.Entry(main_frame, textvariable=rate_var, width=30).pack(padx=10, pady=2)

    tk.Label(main_frame, text="Code:").pack(anchor="w", padx=10)
    tk.Entry(main_frame, textvariable=code_var, width=30).pack(padx=10, pady=2)

    tk.Label(main_frame, text="Currency:").pack(anchor="w", padx=10)
    tk.Entry(main_frame, textvariable=currency_var, width=30).pack(padx=10, pady=2)

    # --- Add Product Handler ---
    def add_product():
        name = name_var.get().strip()
        rate = rate_var.get().strip()
        code = code_var.get().strip()
        currency = currency_var.get().strip()

        if not name or not rate or not code or not currency:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        try:
            rate = float(rate)
        except ValueError:
            messagebox.showerror("Input Error", "Rate must be a number.")
            return

        try:
            conn = sqlite3.connect("db/store.db")
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO products (name, rate, code, currency)
                VALUES (?, ?, ?, ?)
            """, (name, rate, code, currency))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Product '{name}' added successfully.")
            name_var.set("")
            rate_var.set("")
            code_var.set("")
            currency_var.set("INR")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to add product.\n{e}")

    # --- Submit Button ---
    tk.Button(main_frame, text="➕ Add Product", command=add_product, bg="blue", fg="white").pack(pady=15)
