import sqlite3

conn = sqlite3.connect("db/store.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    rate REAL NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT CHECK(role IN ('admin', 'staff')) NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    qty INTEGER,
    rate REAL,
    total REAL,
    date TEXT DEFAULT CURRENT_DATE
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS batches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    batch TEXT NOT NULL,
    expiry DATE
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    items TEXT,
    total REAL,
    bill_date TEXT DEFAULT CURRENT_DATE
)
""")

cur.execute("INSERT OR IGNORE INTO products (name, rate) VALUES ('Milk', 20)")
cur.execute("INSERT OR IGNORE INTO products (name, rate) VALUES ('Bread', 25)")
cur.execute("INSERT OR IGNORE INTO products (name, rate) VALUES ('Butter', 60)")

cur.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin')")
cur.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('staff', 'staff123', 'staff')")

conn.commit()
conn.close()
print("✅ Database initialized successfully with dummy data.")
