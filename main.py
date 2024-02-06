from tkinter import *
import math


def click(num):
    current = display.get()
    display.delete(0, END)
    display.insert(END, current + num)


def clear_entry():
    display.delete(0, END)


def all_clear():
    display.delete(0, END)
    mem_clear()


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(END, result)
    except Exception as e:
        display.delete(0, END)
        display.insert(END, "Error")


def mem_clear():
    global memory
    memory = 0


def mem_add():
    global memory
    try:
        value = float(display.get())
        memory += value
    except ValueError:
        pass


def mem_subtract():
    global memory
    try:
        value = float(display.get())
        memory -= value
    except ValueError:
        pass


def mem_recall():
    display.delete(0, END)
    display.insert(END, memory)


def change_sign():
    current = display.get()
    if current.startswith('-'):
        display.delete(0)
        display.insert(END, current[1:])
    else:
        display.insert(0, '-')


def factorial():
    try:
        value = int(display.get())
        result = math.factorial(value)
        display.delete(0, END)
        display.insert(END, result)
    except ValueError:
        display.delete(0, END)
        display.insert(END, "Error")


def calculate_sqrt():
    try:
        value = float(display.get())
        result = math.sqrt(value)
        display.delete(0, END)
        display.insert(END, result)
    except ValueError:
        display.delete(0, END)
        display.insert(END, "Error")


def calculate_power():
    try:
        value = float(display.get())
        result = value ** 2
        display.delete(0, END)
        display.insert(END, result)
    except ValueError:
        display.delete(0, END)
        display.insert(END, "Error")


root = Tk()
root.title("Calculator")

display = Entry(root, width=50, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4)

buttons = [
    "mc", "m+", "m-", "mr",
    "CE", "AC", "+/-", "!",
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "√", "^"
]


def button_click(number):
    if number == "=":
        calculate()
    elif number == "CE":
        clear_entry()
    elif number == "AC":
        all_clear()
    elif number == "+/-":
        change_sign()
    elif number == "!":
        factorial()
    elif number == "mc":
        mem_clear()
    elif number == "m+":
        mem_add()
    elif number == "m-":
        mem_subtract()
    elif number == "mr":
        mem_recall()
    elif number == "√":
        calculate_sqrt()
    elif number == "^":
        calculate_power()
    else:
        click(number)


row = 1
col = 0

for button in buttons:
    btn = Button(root, text=button, padx=10, pady=10, command=lambda button=button: button_click(button))
    btn.grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
