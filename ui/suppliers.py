# suppliers.py content goes here
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def open_suppliers():
    win = tk.Toplevel()
    win.title("Supplier Management")
    win.geometry("600x400")

    name_var = tk.StringVar()
    contact_var = tk.StringVar()

    # Input Form
    tk.Label(win, text="Supplier Name").pack(pady=5)
    tk.Entry(win, textvariable=name_var).pack()

    tk.Label(win, text="Contact Details").pack(pady=5)
    tk.Entry(win, textvariable=contact_var).pack()

    def add_supplier():
        name = name_var.get().strip()
        contact = contact_var.get().strip()

        if not name:
            messagebox.showerror("Input Error", "Supplier name is required.")
            return

        try:
            conn = sqlite3.connect("../db/store.db")
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS suppliers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, contact TEXT)")
            cur.execute("INSERT INTO suppliers (name, contact) VALUES (?, ?)", (name, contact))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Supplier added successfully!")
            name_var.set("")
            contact_var.set("")
            load_suppliers()
        except Exception as e:
            messagebox.showerror("DB Error", str(e))

    tk.Button(win, text="Add Supplier", command=add_supplier).pack(pady=10)

    # Table to view suppliers
    cols = ("ID", "Name", "Contact")
    tree = ttk.Treeview(win, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=180, anchor="center")
    tree.pack(expand=True, fill='both', padx=10, pady=10)

    def load_suppliers():
        for row in tree.get_children():
            tree.delete(row)
        try:
            conn = sqlite3.connect("../db/store.db")
            cur = conn.cursor()
            cur.execute("SELECT id, name, contact FROM suppliers")
            rows = cur.fetchall()
            for r in rows:
                tree.insert("", "end", values=r)
            conn.close()
        except:
            pass

    load_suppliers()
