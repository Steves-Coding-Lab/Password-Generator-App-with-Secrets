import string
import secrets
import customtkinter as ctk
from tkinter import messagebox
import math


#Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

main_win = ctk.CTk()
main_win.title("Password Generator")
main_win.geometry("700x400")

frame = ctk.CTkFrame(main_win, fg_color="transparent")
frame.pack(padx=50, pady=50)

alphabet = string.ascii_letters + string.digits + string.punctuation
min_pass_len = 10
max_pass_len = 32
median_pass_value = math.floor(((max_pass_len - min_pass_len)/2) + min_pass_len)
light_red = "#fa5959"
dark_red = "#fe2e2e"


def update_slider_value(value):
    value_label.configure(text=str(math.floor(value)))
    pass_length = int(value)
    password = ""
    main_win.clipboard_clear()
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(pass_length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    new_password.delete(0, 'end')
    new_password.insert(0, password)
    
def copy_to_clipboard():
    messagebox.showinfo("Pop-up", "Password Copied to Clipboard")
    pswd = new_password.get() 
    main_win.clipboard_append(pswd)


title_label = ctk.CTkLabel(frame,text="Password Generator", font=('Arial',40))
title_label.grid(row=0, column=0, columnspan=2,  sticky="ew", padx=20, pady=20)

choose_length = ctk.CTkLabel(frame,text="Choose Password Length: ", font=('Arial',18))
choose_length.grid(row=1, column=0, padx=5, pady=20)

password_length_scale = ctk.CTkSlider(frame, from_=min_pass_len, to=max_pass_len, width=200, progress_color="green", command=update_slider_value)
password_length_scale.grid(row=1, column=1)

#display slider value
value_label = ctk.CTkLabel(frame, text=str(median_pass_value), font=('Arial', 16))
value_label.grid(row=1, column=2, padx=5, pady=20)

new_password= ctk.CTkEntry(frame,show="", font=('Arial', 16),width=400)
new_password.grid(row=2, column=0, columnspan=3, padx=5, pady=10)

copy_pass_button = ctk.CTkButton(frame, text="Copy Password", font=('Arial', 14), fg_color=light_red, hover_color=dark_red, command=copy_to_clipboard)
copy_pass_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)


#Populate password field upon loading
update_slider_value(median_pass_value)

main_win.mainloop()


