import tkinter as tk
from tkinter import ttk, messagebox
from send_email import send_email
from receive_email import receive_email
from push_notification import notify

def send_email_gui():
    sender_email = sender_email_entry.get()
    password = password_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    if not all([sender_email, password, recipient_email, subject, body]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        send_email(sender_email, password, recipient_email, subject, body)
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def receive_email_gui():
    email = sender_email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showerror("Error", "Please enter both email and password")
        return

    try:
        message = receive_email(email, password)
        print(message)
        body_text.delete("1.0", tk.END)
        body_text.insert(tk.END, message)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main window
root = tk.Tk()
root.title("Saouda's Mail")
root.geometry("800x600")

# Set wallpaper
wallpaper = tk.PhotoImage(file="1.png")
wallpaper_label = tk.Label(root, image=wallpaper)
wallpaper_label.place(relwidth=1, relheight=1)

sender_email_label = ttk.Label(root, text="Sender's Email:")
sender_email_label.place(x=50, y=50)
sender_email_entry = ttk.Entry(root, width=80)
sender_email_entry.place(x=200, y=50)

password_label = ttk.Label(root, text="Password:")
password_label.place(x=50, y=100)
password_entry = ttk.Entry(root, show="*", width=80)
password_entry.place(x=200, y=100)

recipient_email_label = ttk.Label(root, text="Recipient's Email:")
recipient_email_label.place(x=50, y=150)
recipient_email_entry = ttk.Entry(root, width=80)
recipient_email_entry.place(x=200, y=150)

subject_label = ttk.Label(root, text="Subject:")
subject_label.place(x=50, y=200)
subject_entry = ttk.Entry(root, width=80)
subject_entry.place(x=200, y=200)

body_label = ttk.Label(root, text="Body:")
body_label.place(x=50, y=250)
body_text = tk.Text(root, height=10, width=60)
body_text.place(x=200, y=250)


# Increase button size by adding padding
send_button_style = ttk.Style()
send_button_style.configure("Send.TButton", padding=(20, 10))  # Increase padding to make button larger
send_button = ttk.Button(root, text="Send Email", command=send_email_gui, style="Send.TButton")
send_button.place(x=200, y=500)

receive_button_style = ttk.Style()
receive_button_style.configure("Receive.TButton", padding=(20, 10))  # Increase padding to make button larger
receive_button = ttk.Button(root, text="Receive Email", command=receive_email_gui, style="Receive.TButton")
receive_button.place(x=565, y=500)


# Run the application
root.mainloop()
