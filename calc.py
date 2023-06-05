from _ast import Lambda
from tkinter import *
from math import *
root = Tk()


# defining title of the project
root.title("Simple Calculator")


# button click
def button_click(number):
    global exps
    exps = exps + str(number)
    exp_txt.set(exps)

# button clear


def button_clear():
    global exps
    exps = ""
    exp_txt.set("")


def button_equal():
    global exps
    try:
        output = str(eval(exps))
        exp_txt.set(output)
    except:
        if (ZeroDivisionError):
            exp_txt.set('∞')


def sin_calc():
    global exps
    value = eval(f"round(sin(radians({exps})),1)")
    print(sinh(30))
    exp_txt.set(str(value))


def cos_calc():
    global exps
    value = eval(f"round(cos(radians({exps})),1)")
    print(sinh(30))
    exp_txt.set(str(value))


def tan_calc():
    global exps
    value = eval(f"tan(radians({exps}))")
    if (value > 1):
        exp_txt.set('∞')
    else:
        exp_txt.set(str(value))


def sqrtMethod():
    global exps
    value = eval(f"sqrt({exps})")
    exp_txt.set(str(value))


def back_space():
    global exps
    val = str(exps)
    upVal = val[:-1]
    exps = upVal
    exp_txt.set(exps)


exps = ""
exp_txt = StringVar()
# Defining the buttons

e = Entry(root, width=35, textvariable=exp_txt, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


button_1 = Button(root, text="1", padx=40, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20,
                  command=lambda: button_click(0))
button_dot = Button(root, text=".", padx=40, pady=20,
                    command=lambda: button_click('.'))
button_add = Button(root, text="+", padx=39, pady=20,
                    command=lambda: button_click("+"))
button_subtract = Button(root, text="-", padx=39, pady=20,
                         command=lambda: button_click("-"))
button_multiply = Button(root, text="*", padx=39, pady=20,
                         command=lambda: button_click("*"))
button_divide = Button(root, text="/", padx=39, pady=20,
                       command=lambda: button_click("/"))
button_equal = Button(root, text="=", padx=91, pady=20,
                      command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20,
                      command=button_clear)
button_sin = Button(root, text="Sin", padx=40, pady=20,
                    command=sin_calc
                    )
button_cos = Button(root, text="Cos", padx=40, pady=20,
                    command=cos_calc
                    )
button_tan = Button(root, text="Tan", padx=40, pady=20,
                    command=tan_calc
                    )
button_sqrt = Button(root, text="√", padx=40, pady=20,
                     command=sqrtMethod
                     )
button_square = Button(root, text="^", padx=40, pady=20,
                       command=lambda: button_click("**")
                       )
button_back = Button(root, text="⌫", padx=40, pady=20,
                     command=back_space
                     )

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_dot.grid(row=8, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_subtract.grid(row=5, column=1)
button_multiply.grid(row=5, column=2)
button_divide.grid(row=6, column=0)
button_sin.grid(row=6, column=1)
button_cos.grid(row=6, column=2)
button_tan.grid(row=7, column=0)
button_sqrt.grid(row=7, column=1)
button_square.grid(row=8, column=1)
button_equal.grid(row=7, column=2)
button_back.grid(row=8, column=2)


root.mainloop()
