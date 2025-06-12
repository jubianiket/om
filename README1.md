
# 🛍️ Store Management Software (PC-based)

A complete inventory, billing, purchase, and sales management system built using **Python + Tkinter + SQLite**, designed for offline usage in small shops or businesses.

---

## ✅ Features

- 👨‍💼 Login System (Admin/Staff roles)
- 📦 Inventory Management (Add/Edit Stock)
- 🧾 Billing with GST and Thermal Printing
- 📈 Sales Dashboard (Top Products Chart)
- 🛒 Purchase Entry Module (Stock Inward)
- 🏭 Supplier Management
- 📊 Sales Report Viewer
- ⏳ Batch & Expiry Tracking

---

## 📂 Project Structure

```
store_management_app/
├── db/                 # SQLite database
├── logic/              # Business logic and DB setup
├── ui/                 # UI scripts (Tkinter)
└── main.py             # Entry point (in ui folder)
```

---

## 🧰 Requirements

- Python 3.7+ installed
- Install required package:
```bash
pip install matplotlib
```

---

## 🚀 How to Run

1. Extract the ZIP and open terminal:
```bash
cd store_management_app/ui
python main.py
```

2. Login using default credentials:
```
Username: admin
Password: admin123
```

---

## 💡 Notes

- Database (`store.db`) is stored inside `db/` folder.
- Bills print using default system printer (Thermal 58mm or 80mm).
- Add new staff users via the database manually or extend the UI.

---

## 📌 Future Ideas

- Android sync (Flutter + Firebase)
- CSV/Excel export of reports
- Low stock / expiry alerts
- Customer tracking and loyalty

---

Built with ❤️ using Tkinter.
