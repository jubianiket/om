# billing.py content goes here
import tkinter as tk
import sqlite3

def open_billing():
    win = tk.Toplevel()
    win.title("Billing")
    win.geometry("500x400")

    def load_products():
        conn = sqlite3.connect("../db/store.db")
        cur = conn.cursor()
        cur.execute("SELECT name, rate FROM products")
        products = cur.fetchall()
        conn.close()

        for name, rate in products:
            box.insert(tk.END, f"{name} - ₹{rate}")

    def generate_bill():
        selection = box.curselection()
        items = [box.get(i) for i in selection]
        total = sum(float(i.split("₹")[1]) for i in items)
        total_lbl.config(text=f"Total: ₹{total}")

    box = tk.Listbox(win, selectmode=tk.MULTIPLE, width=50)
    box.pack(pady=10)
    load_products()

    tk.Button(win, text="Generate Bill", command=generate_bill).pack(pady=5)
    total_lbl = tk.Label(win, text="Total: ₹0")
    total_lbl.pack()
