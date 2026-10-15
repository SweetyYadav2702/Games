import tkinter as tk

def add():
    a = int(num1.get())
    b = int(num2.get())

    result.config(text="Result = " + str(a + b))


def sub():
    a = int(num1.get())
    b = int(num2.get())

    result.config(text="Result = " + str(a - b))

def mul():
    a = int(num1.get())
    b = int(num2.get())
    
    result.config(text= "Result = " + str(a * b))
    
def div():
    a = int(num1.get())
    b = int(num2.get())
    
    result.config(text="Result = " + str(a / b))
    
window = tk.Tk()

window.title("My Calculator")
window.geometry("400x300")

tk.Label(window, text="Enter First Number").pack()

num1 = tk.Entry(window)
num1.pack()

tk.Label(window, text="Enter Second Number").pack()

num2 = tk.Entry(window)
num2.pack()

tk.Button(window, text="ADD", command=add).pack(side="left" , padx=10)

tk.Button(window, text="SUB", command=sub).pack(side="left", padx=10)

tk.Button(window, text="Multiply", command=mul).pack(side="left", padx=10)

tk.Button(window, text="DIV", command=div).pack(side="left", padx=10)

result = tk.Label(window, text="Result = ")
result.pack(side="left", padx=50)

window.mainloop()
