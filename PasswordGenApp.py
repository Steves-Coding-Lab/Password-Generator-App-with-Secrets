import string
import secrets
from tkinter import *

main_win = Tk()
main_win.title("Password Generator")
main_win.geometry("600x500")

frame = Frame(main_win)
frame.pack()


alphabet = string.ascii_letters + string.digits + string.punctuation

while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    #print(password)
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break

def gen_pass():   
    pass_length = password_length_scale.get()
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(pass_length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    new_password.delete(0, 'end')
    new_password.insert(0, password)
    
def copy_to_clipboard():
    main_win.clipboard_clear()
    pswd = new_password.get() #Just incase user modifies password further
    main_win.clipboard_append(pswd)


title_label = Label(frame,text="Password Generator", font=('Arial',30))
title_label.grid(row=0, column=0, columnspan=2,  sticky="news", pady=40)

choose_length = Label(frame,text="Choose Password Length: ", font=('Arial',14))
choose_length.grid(row=1, column=0)

password_length_scale = Scale(frame, orient='horizontal', from_=8, to=32, length=150)
password_length_scale.grid(row=1, column=1)

generate_pass_button = Button(frame, text="Generate Password", font=('Arial', 14), command=gen_pass)
generate_pass_button.grid(row=2, column=0, columnspan=2, pady=20)

new_password= Entry(frame,show="", font=('Arial', 12),width=35)
new_password.grid(row=3, column=0, columnspan=2, pady=20)

copy_pass_button = Button(frame, text="Copy Password", font=('Arial', 14), command=copy_to_clipboard)
copy_pass_button.grid(row=4, column=0, columnspan=2, pady=20)

main_win.mainloop()


