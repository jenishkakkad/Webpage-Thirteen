import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

def register():
    username = entry_reg_username.get()
    password = entry_reg_password.get()
    #first_name = entry_first_name.get()
    #last_name = entry_last_name.get()
    #gender = gender_var.get()
    #age = entry_age.get()
   # address = entry_address.get()
    #username = entry_reg_username.get()
    #password = entry_reg_password.get()
        
    # Check if username already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = c.fetchone()
    if existing_user:
        messagebox.showerror("Registration", "Username already exists")
        return

    # Insert new user into the database
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

    messagebox.showinfo("Registration", "Registration successful")

def login():
    username = entry_login_username.get()
    password = entry_login_password.get()

    # Query the database for the entered username and password
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    if user:
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login", "Invalid username or password")

def toggle_forms():
    if registration_frame.winfo_ismapped():
        registration_frame.grid_remove()
        login_frame.grid()
    else:
        login_frame.grid_remove()
        registration_frame.grid()

# Create main application window
root = tk.Tk()
root.title("Registration and Login")

# Create registration frame
registration_frame = tk.Frame(root)
registration_frame.grid(row=0, column=0, padx=5, pady=5)

#label_first_name = tk.Label(registration_frame, text="First Name")
#label_first_name.grid(row=0, column=0, padx=5, pady=5)
#entry_first_name = tk.Entry(registration_frame)
#entry_first_name.grid(row=0, column=1, padx=5, pady=5)

#label_last_name = tk.Label(registration_frame, text="Last Name")
#label_last_name.grid(row=1, column=0, padx=5, pady=5)
#entry_last_name = tk.Entry(registration_frame)
#entry_last_name.grid(row=1, column=1, padx=5, pady=5)

#label_gender = tk.Label(registration_frame, text="Gender")
#label_gender.grid(row=2, column=0, padx=5, pady=5)
#gender_var = tk.StringVar()
#gender_var.set("Male")  # Default gender selection
#male_radio = tk.Radiobutton(registration_frame, text="Male", variable=gender_var, value="Male")
#male_radio.grid(row=2, column=1, padx=5, pady=5)
#female_radio = tk.Radiobutton(registration_frame, text="Female", variable=gender_var, value="Female")
#female_radio.grid(row=2, column=2, padx=5, pady=5)

#label_age = tk.Label(registration_frame, text="Age")
#label_age.grid(row=3, column=0, padx=5, pady=5)
#entry_age = tk.Entry(registration_frame)
#entry_age.grid(row=3, column=1, padx=5, pady=5)

#label_address = tk.Label(registration_frame, text="Address")
#label_address.grid(row=4, column=0, padx=5, pady=5)
#entry_address = tk.Entry(registration_frame)
#entry_address.grid(row=4, column=1, padx=5, pady=5)

label_reg_username = tk.Label(registration_frame, text="Username")
label_reg_username.grid(row=5, column=0, padx=5, pady=5)
entry_reg_username = tk.Entry(registration_frame)
entry_reg_username.grid(row=5, column=1, padx=5, pady=5)

label_reg_password = tk.Label(registration_frame, text="Password")
label_reg_password.grid(row=6, column=0, padx=5, pady=5)
entry_reg_password = tk.Entry(registration_frame, show="*")
entry_reg_password.grid(row=6, column=1, padx=5, pady=5)

register_button = tk.Button(registration_frame, text="Register", command=register)
register_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)



# Create login frame
login_frame = tk.Frame(root)
login_frame.grid(row=0, column=0, padx=5, pady=5)

label_login_username = tk.Label(login_frame, text="Username")
label_login_username.grid(row=0, column=0, padx=5, pady=5)
entry_login_username = tk.Entry(login_frame)
entry_login_username.grid(row=0, column=1, padx=5, pady=5)

label_login_password = tk.Label(login_frame, text="Password")
label_login_password.grid(row=1, column=0, padx=5, pady=5)
entry_login_password = tk.Entry(login_frame, show="*")
entry_login_password.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create toggle button
toggle_button = tk.Button(root, text="Switch to Register" if registration_frame.winfo_ismapped() else "Switch to Login", command=toggle_forms)
toggle_button.grid(row=1, column=0, padx=5, pady=5)

# Start with the registration frame displayed
login_frame.grid_remove()
registration_frame.grid()

# Run the main event loop
root.mainloop()

# Close database connection
conn.close()
