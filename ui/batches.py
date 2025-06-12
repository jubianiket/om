# batches.py content goes here
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import datetime

def open_batches():
    win = tk.Toplevel()
    win.title("Batch & Expiry Tracking")
    win.geometry("700x500")

    product_var = tk.StringVar()
    batch_var = tk.StringVar()
    expiry_var = tk.StringVar()

    # Form Fields
    tk.Label(win, text="Product Name").pack(pady=5)
    tk.Entry(win, textvariable=product_var).pack()

    tk.Label(win, text="Batch No.").pack(pady=5)
    tk.Entry(win, textvariable=batch_var).pack()

    tk.Label(win, text="Expiry Date (YYYY-MM-DD)").pack(pady=5)
    tk.Entry(win, textvariable=expiry_var).pack()

    def add_batch():
        product = product_var.get().strip()
        batch = batch_var.get().strip()
        expiry = expiry_var.get().strip()

        # Validation
        try:
            datetime.datetime.strptime(expiry, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Expiry must be YYYY-MM-DD")
            return

        if not product or not batch:
            messagebox.showerror("Missing Fields", "Please enter product and batch number.")
            return

        try:
            conn = sqlite3.connect("../db/store.db")
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS batches (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product TEXT,
                    batch TEXT,
                    expiry DATE
                )
            """)
            cur.execute("INSERT INTO batches (product, batch, expiry) VALUES (?, ?, ?)", (product, batch, expiry))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Batch added.")
            product_var.set("")
            batch_var.set("")
            expiry_var.set("")
            load_batches()
        except Exception as e:
            messagebox.showerror("DB Error", str(e))

    tk.Button(win, text="Add Batch", command=add_batch).pack(pady=10)

    # Table for viewing batches
    cols = ("ID", "Product", "Batch", "Expiry")
    tree = ttk.Treeview(win, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=150)
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    def load_batches():
        for row in tree.get_children():
            tree.delete(row)
        try:
            conn = sqlite3.connect("../db/store.db")
            cur = conn.cursor()
            cur.execute("SELECT id, product, batch, expiry FROM batches ORDER BY expiry ASC")
            rows = cur.fetchall()
            for row in rows:
                tree.insert("", "end", values=row)
            conn.close()
        except:
            pass

    load_batches()
