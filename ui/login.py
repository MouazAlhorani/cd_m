import customtkinter as ctk
import sqlite3
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x600")
app.title("Login")

# Container (كرت بالمنتصف)
frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(pady=20, padx=20, fill="both", expand=True)

title = ctk.CTkLabel(frame, text="Welcome Back", font=ctk.CTkFont(size=22, weight="bold"))
title.pack(pady=(20,10))

subtitle = ctk.CTkLabel(frame, text="Login to your account", font=ctk.CTkFont(size=12))
subtitle.pack(pady=(0,20))

username_entry = ctk.CTkEntry(frame, placeholder_text="Username")
username_entry.pack(pady=10, padx=20, fill="x")

password_entry = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
password_entry.pack(pady=10, padx=20, fill="x")

def login():
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        status_label.configure(text="✅ user has access", text_color="green")
    else:
        status_label.configure(text="❌ user hasn't access", text_color="red")

login_btn = ctk.CTkButton(frame, text="Login", command=login,font=ctk.CTkFont(size=20))
login_btn.pack(pady=20, padx=20, fill="x")


def admin_login():
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=? AND role='admin'",
        (username, password)
    )

    admin = cursor.fetchone()
    conn.close()

    if admin:
        status_label.configure(text="✅ Admin login successful", text_color="green")
    else:
        status_label.configure(text="❌ Invalid admin credentials", text_color="red")

admin_btn = ctk.CTkButton(
    frame,
    text="Admin Login",
    fg_color="gray",
    hover_color="#8F2B2B",
    command=admin_login,
    font=ctk.CTkFont(size=18)
)
admin_btn.pack(pady=5, padx=20, fill="x")




status_label = ctk.CTkLabel(frame, text="", font=ctk.CTkFont(size=15))
status_label.pack(pady=(5,10))

app.mainloop()