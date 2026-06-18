import sqlite3
import bcrypt

# 1. Database aur Table Setup
conn = sqlite3.connect("smartvault.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

# 2. Naya User Register Karne Ka Function (With Encryption)
def register_user(username, password):
    # Password ko bytes mein badal kar hash (encrypt) karna
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    try:
        # Hashed password ko database mein save kar rahe hain
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print(f"✨ User '{username}' successfully encrypted password ke sath register ho gaya hai!")
    except sqlite3.IntegrityError:
        print(f"❌ Error: '{username}' naam ka user pehle se exist karta hai!")
        raise Exception("User already exists")

# 3. Login Check Karne Ka Function (With Decryption/Verification)
def login_user(username, password):
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if result:
        db_password = result[0] # Database mein save hashed password
        password_bytes = password.encode('utf-8')
        
        # Check karna ki enter kiya gaya password database wale hash se match karta hai ya nahi
        if bcrypt.checkpw(password_bytes, db_password):
            print("🔓 Login Successful! Welcome back.")
            return True
        else:
            print("❌ Login Failed! Password galat hai.")
            return False
    else:
        print("❌ Login Failed! Username nahi mila.")
        return False

# Code test karne ke liye Main Block (Jab direct run karein)
if __name__ == "__main__":
    print("📂 Database aur Tables check ho rahe hain...")