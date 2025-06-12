import tkinter as tk
from login import login_app
from inventory import open_inventory
from billing import open_billing
from sales_report import open_sales_report
from purchase import open_purchase
from suppliers import open_suppliers
from dashboard import open_dashboard
from batches import open_batches

def load_ui_by_role(role):
    root = tk.Tk()
    root.title(f"Store Manager ({role.capitalize()})")
    root.geometry("400x500")

    tk.Label(root, text=f"Welcome {role.capitalize()}", font=("Arial", 18)).pack(pady=10)

    # Features available to all
    tk.Button(root, text="📦 Inventory", width=25, command=open_inventory).pack(pady=5)
    tk.Button(root, text="🧾 Billing", width=25, command=open_billing).pack(pady=5)
    tk.Button(root, text="📊 Sales Report", width=25, command=open_sales_report).pack(pady=5)
    tk.Button(root, text="📈 Dashboard", width=25, command=open_dashboard).pack(pady=5)

    # Only for Admin
    if role == "admin":
        tk.Button(root, text="📥 Purchase Entry", width=25, command=open_purchase).pack(pady=5)
        tk.Button(root, text="🏭 Supplier Management", width=25, command=open_suppliers).pack(pady=5)
        tk.Button(root, text="📦 Batch & Expiry", width=25, command=open_batches).pack(pady=5)

    tk.Button(root, text="🚪 Exit", width=25, command=root.destroy).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    login_app(load_ui_by_role)
