# login.py content goes here
import tkinter as tk
from tkinter import messagebox
import sqlite3

def login_app(callback):
    def handle_login():
        user = username.get()
        pwd = password.get()

        conn = sqlite3.connect("../db/store.db")
        cur = conn.cursor()
        cur.execute("SELECT role FROM users WHERE username=? AND password=?", (user, pwd))
        result = cur.fetchone()
        conn.close()

        if result:
            login_window.destroy()
            callback(result[0])
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x200")

    tk.Label(login_window, text="Username").pack()
    username = tk.Entry(login_window)
    username.pack()

    tk.Label(login_window, text="Password").pack()
    password = tk.Entry(login_window, show="*")
    password.pack()

    tk.Button(login_window, text="Login", command=handle_login).pack(pady=10)
    login_window.mainloop()
