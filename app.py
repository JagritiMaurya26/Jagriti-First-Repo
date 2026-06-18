import tkinter as tk
from tkinter import messagebox
import backend  # Hamari secure backend file

# --- 1. DASHBOARD WINDOW FUNCTION ---
def open_dashboard(username):
    # Nayi Dashboard Window setup
    dash_window = tk.Tk()
    dash_window.title("SmartVault Dashboard - Secure Session")
    dash_window.geometry("600x400")
    dash_window.configure(bg="#121212") # Darker material theme

    # Top Welcome Bar
    welcome_label = tk.Label(
        dash_window, 
        text=f"👋 Welcome to your Vault, {username}!", 
        font=("Arial", 16, "bold"), 
        fg="#007acc", 
        bg="#121212"
    )
    welcome_label.pack(pady=20)

    # Status Card / Frame
    card_frame = tk.Frame(dash_window, bg="#1e1e1e", bd=1, relief="solid")
    card_frame.pack(pady=10, padx=50, fill="both", expand=True)

    status_title = tk.Label(
        card_frame, 
        text="🛡️ Security Status: Fully Encrypted", 
        font=("Arial", 12, "bold"), 
        fg="#4CAF50", 
        bg="#1e1e1e"
    )
    status_title.pack(pady=15)

    # Dummy secure data content inside the vault
    info_text = (
        "🔐 Your Encrypted Files: 0\n\n"
        "🔑 Connected Database: smartvault.db\n\n"
        "🚀 Security Engine: Bcrypt Hashing Active"
    )
    info_label = tk.Label(
        card_frame, 
        text=info_text, 
        font=("Arial", 11), 
        fg="#cccccc", 
        bg="#1e1e1e", 
        justify="left"
    )
    info_label.pack(pady=10)

    # Logout Button
    def logout():
        dash_window.destroy() # Dashboard band karega
        create_login_window() # Wapas login window kholega

    logout_btn = tk.Button(
        dash_window, 
        text="Logout & Lock Vault", 
        font=("Arial", 11, "bold"), 
        bg="#d32f2f", 
        fg="#ffffff", 
        bd=0, 
        command=logout
    )
    logout_btn.pack(pady=20, ipady=5, ipadx=10)

    dash_window.mainloop()


# --- 2. LOGIN WINDOW FUNCTION ---
def create_login_window():
    global root, username_entry, password_entry
    
    root = tk.Tk()
    root.title("SanDisk SmartVault - Security Center")
    root.geometry("400x450")
    root.configure(bg="#1e1e1e")

    title_label = tk.Label(root, text="🔒 SmartVault Login", font=("Arial", 18, "bold"), fg="#ffffff", bg="#1e1e1e")
    title_label.pack(pady=30)

    username_label = tk.Label(root, text="Username:", font=("Arial", 11), fg="#cccccc", bg="#1e1e1e")
    username_label.pack(anchor="w", padx=50)
    username_entry = tk.Entry(root, font=("Arial", 12), width=25, bg="#2d2d2d", fg="#ffffff", insertbackground="white", bd=0)
    username_entry.pack(pady=5, ipady=5)

    password_label = tk.Label(root, text="Password:", font=("Arial", 11), fg="#cccccc", bg="#1e1e1e")
    password_label.pack(anchor="w", padx=50, pady=(10, 0))
    password_entry = tk.Entry(root, font=("Arial", 12), width=25, bg="#2d2d2d", fg="#ffffff", insertbackground="white", bd=0, show="*")
    password_entry.pack(pady=5, ipady=5)

    # Login Logic
    def handle_login():
        user = username_entry.get()
        pwd = password_entry.get()
        
        if not user or not pwd:
            messagebox.showwarning("Warning", "Sabhi fields bharna zaroori hai!")
            return
            
        success = backend.login_user(user, pwd)
        if success:
            messagebox.showinfo("Success", f"Welcome back, {user}! 🎉\nVault open ho gaya hai.")
            root.destroy()       # 1. Login window ko close karega
            open_dashboard(user) # 2. Naya dashboard kholega
        else:
            messagebox.showerror("Error", "Login Failed! Username ya Password galat hai. ❌")

    # Register Logic
    def handle_register():
        user = username_entry.get()
        pwd = password_entry.get()
        
        if not user or not pwd:
            messagebox.showwarning("Warning", "Username aur Password likhna zaroori hai!")
            return
            
        try:
            backend.register_user(user, pwd)
            messagebox.showinfo("Success", f"User '{user}' successfully register ho gaya! 🚀\nAb aap login kar sakte hain.")
        except Exception as e:
            messagebox.showerror("Error", "Yeh username pehle se exist karta hai ya koi error hai!")

    # Buttons
    login_btn = tk.Button(root, text="Login", font=("Arial", 12, "bold"), bg="#007acc", fg="#ffffff", width=22, bd=0, command=handle_login)
    login_btn.pack(pady=25, ipady=5)

    register_btn = tk.Button(root, text="Naya Account Banayein (Register)", font=("Arial", 10), bg="#1e1e1e", fg="#007acc", bd=0, activebackground="#1e1e1e", activeforeground="#005999", command=handle_register)
    register_btn.pack(pady=5)

    root.mainloop()

# App shuru karne ke liye execution point
if __name__ == "__main__":
    create_login_window()