# Library Imports
from _ast import Lambda
from tkinter import *
from math import *


# Initilazing Tk Class as root
root = Tk()


# Fixed Screen Size
root.resizable(0, 0)

# Icon File
root.iconbitmap("calculator.ico")

# Global Color Configuration
root.config(background="#ffffff")


# Project Title
root.title("Scientific Calculator")


# Function For Input Button
def button_click(number):
    global exps
    exps = exps + str(number)
    exp_txt.set(exps)


# Function For Clear Button
def button_clear():
    global exps
    exps = ""
    exp_txt.set("")


# Function For All Arithmetic Calculation
def button_equal():
    global exps
    try:
        output = str(eval(exps))
        exp_txt.set(output)
    except:
        if (ZeroDivisionError):
            exp_txt.set('∞')


# Function For Sin
def sin_calc():
    global exps
    try:
        value = eval(f"round(sin(radians({exps})),1)")
        exp_txt.set(str(value))
    except:
        if (TypeError):
            exp_txt.set("Invalid Input")


# Function For Cos
def cos_calc():
    global exps
    try:
        value = eval(f"round(cos(radians({exps})),1)")
        exp_txt.set(str(value))
    except:
        if (TypeError):
            exp_txt.set("Invalid Input")


# Function For Tan
def tan_calc():
    global exps
    try:
        value = eval(f"tan(radians({exps}))")
        if (value > 1):
            exp_txt.set('∞')
        else:
            exp_txt.set(str(value))
    except:
        if (TypeError):
            exp_txt.set("Invalid Input")


# Function For Square Root
def sqrtMethod():
    global exps
    try:
        value = eval(f"sqrt({exps})")
        exp_txt.set(str(value))
    except:
        if (TypeError):
            exp_txt.set("Invalid Input")


# Function For Back Space
def back_space():
    global exps
    val = str(exps)
    upVal = val[:-1]
    exps = upVal
    exp_txt.set(exps)


# Global Variable For Input
exps = ""

# Defining Input Type
exp_txt = StringVar()
e = Entry(root, font=('poppins', 26), width=15,
          textvariable=exp_txt, borderwidth=0, highlightthickness=1, highlightcolor="#fff", relief="solid")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)


# All Buttons
button_7 = Button(root, background="#ffffff", activebackground="#ffffff", borderwidth=0, font=('bold'), text="7", padx=31, pady=15,
                  command=lambda: button_click(7))


button_8 = Button(root, background="#ffffff", activebackground="#ffffff",  borderwidth=0, font=('bold'),  text="8", padx=31, pady=15,
                  command=lambda: button_click(8))


button_9 = Button(root, background="#ffffff", activebackground="#ffffff",  borderwidth=0, font=('bold'),  text="9", padx=31, pady=15,
                  command=lambda: button_click(9))


button_back = Button(root, fg="#ffffff", activebackground="#FF702A", activeforeground="#ffffff", background="#FF702A", borderwidth=0, font=('bold'),  text="⌫", padx=30, pady=15,
                     command=back_space)

button_3 = Button(root, background="#ffffff", activebackground="#ffffff",  borderwidth=0, font=('bold'),  text="3", padx=31, pady=15,
                  command=lambda: button_click(3))


button_4 = Button(root, background="#ffffff", activebackground="#ffffff",  borderwidth=0, font=('bold'), text="4", padx=31, pady=15,
                  command=lambda: button_click(4))


button_5 = Button(root, background="#ffffff", activebackground="#ffffff",  borderwidth=0, font=('bold'), text="5", padx=31, pady=15,
                  command=lambda: button_click(5))


button_6 = Button(root, background="#ffffff", activebackground="#ffffff",  borderwidth=0, font=('bold'), text="6", padx=31, pady=15,
                  command=lambda: button_click(6))


button_1 = Button(root, background="#ffffff", activebackground="#ffffff",  borderwidth=0, font=('bold'), text="1", padx=31, pady=15,
                  command=lambda: button_click(1))


button_2 = Button(root, background="#ffffff", activebackground="#ffffff",  borderwidth=0, font=('bold'), text="2", padx=31, pady=15,
                  command=lambda: button_click(2))


button_0 = Button(root, background="#ffffff", activebackground="#ffffff",  borderwidth=0, font=('bold'), text="0", padx=31, pady=15,
                  command=lambda: button_click(0))


button_dot = Button(root, background="#ffffff", fg="#FF702A", borderwidth=0, font=('bold'), text=".", padx=37, pady=15,
                    command=lambda: button_click('.'))


button_add = Button(root, background="#ffffff", activebackground="#ffffff", activeforeground="#FF702A", fg="#FF702A", borderwidth=0, font=('bold'), text="+", padx=34, pady=15,
                    command=lambda: button_click("+"))


button_subtract = Button(root, background="#ffffff", activebackground="#ffffff", activeforeground="#FF702A", fg="#FF702A", borderwidth=0, font=('bold'),  text="-", padx=32, pady=15,
                         command=lambda: button_click("-"))
button_multiply = Button(root, background="#ffffff", activebackground="#ffffff", activeforeground="#FF702A", fg="#FF702A", borderwidth=0, font=('bold'), text="x", padx=31, pady=15,
                         command=lambda: button_click("*"))


button_divide = Button(root, background="#ffffff", activebackground="#ffffff", activeforeground="#FF702A", fg="#FF702A", borderwidth=0, font=('bold'),  text="/", padx=37, pady=15,
                       command=lambda: button_click("/"))


# Sin Button
button_sin = Button(root, background="#ffffff", activebackground="#ffffff", activeforeground="#FF702A", fg="#FF702A", borderwidth=0, font=('bold'),  text="sin", padx=26, pady=15,
                    command=sin_calc)


# Cos Button
button_cos = Button(root, background="#ffffff", activebackground="#ffffff", activeforeground="#FF702A", fg="#FF702A", borderwidth=0, font=('bold'),  text="cos", padx=26, pady=15,
                    command=cos_calc)


# Tan Button
button_tan = Button(root, background="#ffffff", activebackground="#ffffff", activeforeground="#FF702A", fg="#FF702A", borderwidth=0, font=('bold'),  text="tan", padx=26, pady=15,
                    command=tan_calc)


# Square Root Button
button_sqrt = Button(root, background="#ffffff", activebackground="#ffffff", activeforeground="#FF702A", fg="#FF702A", borderwidth=0, text="√", padx=35, pady=15,
                     command=sqrtMethod)


# Power Button
button_square = Button(root, background="#ffffff", activebackground="#ffffff", activeforeground="#FF702A", fg="#FF702A", borderwidth=0, font=('bold'),  text="^", padx=30, pady=15,
                       command=lambda: button_click("**"))


# Calculate Button
button_equal = Button(root, background="#FF702A", justify="center", fg="#ffffff", borderwidth=0, font=('bold'),  text="=", padx=30, pady=15,
                      command=button_equal)


# All Clear Button
button_clear = Button(root, background="#ffffff", fg="#FF702A", activebackground="#ffffff", activeforeground="#FF702A", borderwidth=0, font=('bold'), text="AC", padx=22, pady=15,
                      command=button_clear)


# Modulus Division Button
button_mod = Button(root, background="#ffffff", activebackground="#ffffff", activeforeground="#FF702A", fg="#FF702A", borderwidth=0, font=('bold'),  text="%", padx=30, pady=15,
                    command=lambda: button_click("%"))


# Row 1 Buttons
button_7.grid(row=1, sticky="w", column=0)
button_8.grid(row=1, sticky="w", column=1)
button_9.grid(row=1, sticky="w", column=2)
button_back.grid(row=1, sticky="e", column=3)


# Row 2 Buttons
button_4.grid(row=2, sticky="w", column=0)
button_5.grid(row=2, sticky="w", column=1)
button_6.grid(row=2, sticky="w", column=2)
button_add.grid(row=2, sticky="e", column=3)

# Row 3 Buttons
button_1.grid(row=3, sticky="w", column=0)
button_2.grid(row=3, sticky="w", column=1)
button_3.grid(row=3, sticky="w", column=2)
button_dot.grid(row=3, sticky="e", column=3)

# Row 4 Buttons
button_0.grid(row=4, sticky="w", column=0)
button_subtract.grid(row=4, sticky="w", column=1)
button_multiply.grid(row=4, sticky="w", column=2)
button_divide.grid(row=4, sticky="e", column=3)

# Row 5 Buttons
button_sin.grid(row=5, sticky="w", column=0)
button_cos.grid(row=5, sticky="w", column=1)
button_tan.grid(row=5, sticky="w", column=2)
button_sqrt.grid(row=5, sticky="e", column=3)


# Row 6 Buttons
button_square.grid(row=6, sticky="w", column=0)
button_mod.grid(row=6, sticky="w", column=1)
button_clear.grid(row=6, sticky="w", column=2)
button_equal.grid(row=6, sticky="e", column=3)


root.mainloop()
