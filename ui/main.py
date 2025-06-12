import tkinter as tk
from login import login_app
from inventory import open_inventory
from billing import open_billing
from sales_report import open_sales_report
from purchase import open_purchase
from suppliers import open_suppliers
from dashboard import open_dashboard
from batches import open_batches


def clear_main_frame(main_frame):
 for widget in main_frame.winfo_children():
  widget.destroy()

def show_frame(frame_func, main_frame):
 clear_main_frame(main_frame)
 # Pass the main_frame to the function so it can place its content there
 frame_func(main_frame)


def load_ui_by_role(role):
    root = tk.Tk()
    root.title(f"Store Manager ({role.capitalize()})")
    root.geometry("600x500")  # Increase window width to accommodate nav bar

    # Use grid layout for the main window
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1) # Configure column 1 to expand

    # Navigation bar frame
    nav_frame = tk.Frame(root, width=150, bg="lightgray")
    nav_frame.grid(row=0, column=0, sticky="ns") # Place nav_frame on the left, spanning rows
    nav_frame.grid_propagate(False) # Prevent frame from shrinking to fit widgets

 # Main content frame
 main_frame = tk.Frame(root, bg="white")
 main_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10) # Place main_frame on the right

    tk.Label(nav_frame, text="Navigation", font=("Arial", 14, "bold"), bg="lightgray").pack(pady=10)

    # Features available to all
    tk.Button(nav_frame, text="📦 Inventory", width=20, command=lambda: show_frame(open_inventory, main_frame)).pack(pady=5, padx=10)
    tk.Button(nav_frame, text="🧾 Billing", width=20, command=lambda: show_frame(open_billing, main_frame)).pack(pady=5, padx=10)
    tk.Button(nav_frame, text="📊 Sales Report", width=20, command=lambda: show_frame(open_sales_report, main_frame)).pack(pady=5, padx=10)
    tk.Button(nav_frame, text="📈 Dashboard", width=20, command=lambda: show_frame(open_dashboard, main_frame)).pack(pady=5, padx=10)

    # Only for Admin
    if role == "admin":
        tk.Button(nav_frame, text="📥 Purchase Entry", width=20, command=lambda: show_frame(open_purchase, main_frame)).pack(pady=5, padx=10)
        tk.Button(nav_frame, text="🏭 Supplier Management", width=20, command=lambda: show_frame(open_suppliers, main_frame)).pack(pady=5, padx=10)
        tk.Button(nav_frame, text="📦 Batch & Expiry", width=20, command=lambda: show_frame(open_batches, main_frame)).pack(pady=5, padx=10)

    tk.Button(nav_frame, text="🚪 Exit", width=20, command=root.destroy).pack(pady=20, padx=10)

    root.mainloop()

if __name__ == "__main__":
    login_app(load_ui_by_role)