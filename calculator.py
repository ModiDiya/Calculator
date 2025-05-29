import tkinter as tk

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Creative Calculator")
    window.geometry("500x600")
    window.configure(bg="#2C3E50")
    window.resizable(True, True)  # Allow window resizing

    expression = ""
    equation = tk.StringVar()

    # Configure grid weights to expand on resize
    for i in range(6):
        window.rowconfigure(i, weight=1)
    for j in range(4):
        window.columnconfigure(j, weight=1)

    entry_field = tk.Entry(
        window, textvariable=equation, font=('Segoe UI', 30),
        bd=10, insertwidth=2, borderwidth=5, relief='sunken',
        justify='right', bg="#ECF0F1"
    )
    entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('C', 5, 0)
    ]

    for (text, row, col) in buttons:
        if text == '=':
            tk.Button(
                window, text=text, font=('Segoe UI', 20),
                bg="#1ABC9C", fg="white", command=equalpress
            ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        elif text == 'C':
            tk.Button(
                window, text=text, font=('Segoe UI', 20),
                bg="#E74C3C", fg="white", command=clear
            ).grid(row=row, column=col, columnspan=4, padx=5, pady=5, sticky="nsew")
        else:
            tk.Button(
                window, text=text, font=('Segoe UI', 20),
                bg="#34495E", fg="white", command=lambda t=text: press(t)
            ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    window.mainloop()
