import tkinter as tk

window = tk. Tk()
window.title("Bea's Profile")
window.geometry("600x600")
window.resizable(True, True)
window.configure(bg="lightpink")

studentprofile_label = tk.Label(window, text="Student Profile", font=("Arial", 35, "bold"), bg="lightpink")
fullname_label = tk.Label(window, text=" Name: Beatrice Z. Cadiz", font=("Arial", 18), bg="lightpink")
age_label = tk.Label(window, text=" Age: 18", font=("Arial", 18), bg="lightpink")
course_label = tk. Label(window, text=" Course: BSIT", font=("Arial", 18), bg="lightpink")
birthday_label = tk.Label(window, text=" Birthday: June 12, 2007", font=("Arial", 18), bg="lightpink")
motto_label = tk. Label(window, text=" Motto:", font=("Arial", 18), bg="lightpink")
quote_label = tk. Label(window, text="    \"Pasa lang nang pasa, Bahala na. \"", font=("Arial", 18, "italic"), bg="lightpink")

studentprofile_label.pack(pady=20)
fullname_label.pack(pady=10, anchor="w")
age_label.pack(pady=10, anchor="w")
course_label.pack(pady=10, anchor="w")
birthday_label.pack(pady=10, anchor="w")
motto_label.pack(pady=10, anchor="w") 
quote_label.pack(pady=10, anchor="w")

window.mainloop()
