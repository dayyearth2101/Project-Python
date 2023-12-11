import tkinter as tk
from tkinter import messagebox

# C = (F-32)*5/9
# F = (9/5)*C + 32

font_family = ("Time New Roman", 16, "bold")

def convert():
    try:
        val = var.get()
        tmp = float(temp.get())
    
        if val == 1:
            f_temp = (9/5)*tmp + 32
            result = f"{tmp} C = {f_temp:.2f} F"
        elif val == 2:
            c_temp = (tmp-32) * (5/9)
            result = f"{tmp} F = {c_temp:.2f} C"
        
        messagebox.showinfo("Result: ", result)
    except Exception as e:
        messagebox.showerror("Error: ", e)

root = tk.Tk()
root.title("Temperature convert")
root.geometry("650x150")

frame = tk.Frame(root)
frame.pack(pady = 20)

tk.Label(frame, text="Temperature", font=font_family).grid(row=0, column=0)
temp = tk.Entry(frame, width= 30, font=font_family)
temp.grid(row = 0, column=1, padx=20, pady=10)

tk.Button(frame, text="Convert", command=convert, font=font_family).grid(row=0, column=2)

var = tk.IntVar()
tk.Radiobutton(frame, text="C to F", variable=var, value=1, font=font_family).grid(row=1, column=1)
tk.Radiobutton(frame, text="F to C", variable=var, value=2, font=font_family).grid(row=2, column=1)

root.mainloop()

