from tkinter import *
from datetime import datetime

window = Tk()
window.title("Profile Builder")
window.geometry("500x300")
window.config(bg="pink")

def compute_age(event):
    try:
        year = int(birth_entry.get())
        current_year = datetime.now().year
        age = current_year - year
        age_label.config(text=f"{age} years old")
    except:
        age_label.config(text="Invalid input")

def change_color():
    if gender.get() == "Male":
        window.config(bg="darkblue")
    else:
        window.config(bg="pink")

def on_enter(e):
    submit_btn.config(bg="white")

def on_leave(e):
    submit_btn.config(bg="white")

def generate_id():
    new_window = Toplevel(window)
    new_window.title("Student ID")
    new_window.geometry("300x250")
    new_window.config(bg="pink")

    full_name = f"{fname.get()} {mname.get()} {lname.get()}"
    age = age_label.cget("text")
    gen = gender.get()

    Label(new_window, text="Student ID", font=("Arial", 16, "bold"), bg="pink").pack(pady=10)

    frame = Frame(new_window, bg="lightgray", padx=10, pady=10)
    frame.pack(pady=10)

    Label(frame, text="Name: " + full_name, bg="lightgray").pack(anchor="w")
    Label(frame, text="Age: " + age, bg="lightgray").pack(anchor="w")
    Label(frame, text="Gender: " + gen, bg="lightgray").pack(anchor="w")

fname = StringVar()
mname = StringVar()
lname = StringVar()
gender = StringVar(value="Female")

Label(window, text="Profile Builder", font=("Arial", 16, "bold"), bg="lightgreen").pack(pady=10)

frame = Frame(window, bg="pink")
frame.pack()

Entry(frame, textvariable=fname).grid(row=0, column=0, padx=5)
Entry(frame, textvariable=mname).grid(row=0, column=1, padx=5)
Entry(frame, textvariable=lname).grid(row=0, column=2, padx=5)

Label(frame, text="First Name", bg="lightgreen").grid(row=1, column=0)
Label(frame, text="Middle Name", bg="lightgreen").grid(row=1, column=1)
Label(frame, text="Last Name", bg="lightgreen").grid(row=1, column=2)

birth_entry = Entry(window)
birth_entry.pack(pady=5)
birth_entry.bind("<Return>", compute_age)

Label(window, text="Birth Year", bg="lightgreen").pack()

age_label = Label(window, text="Computing Age...", bg="lightgreen")
age_label.pack()

Label(window, text="Gender", bg="lightgreen").pack()

Radiobutton(window, text="Male", variable=gender, value="Male", command=change_color, bg="lightgreen").pack()
Radiobutton(window, text="Female", variable=gender, value="Female", command=change_color, bg="lightgreen").pack()

submit_btn = Button(window, text="Submit", command=generate_id, bg="white")
submit_btn.pack(pady=10)

submit_btn.bind("<Enter>", on_enter)
submit_btn.bind("<Leave>", on_leave)

window.mainloop()