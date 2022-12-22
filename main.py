# import the module
import tkinter

# Creating the Functions
def button_click(number):
    current = e.get()
    e.delete(0, "end")
    e.insert(0, str(current) + str(number))


def button_point():
    global current
    first = e.get()
    e.delete(0, "end")
    e.insert(0, str(first) + ".")


def button_sign():
    first = float(e.get())
    e.delete(0, "end")
    e.insert(0, first * (-1))


def button_opp(opp):
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    global operator
    operator = str(opp)
    e.delete(0, "end")


def button_equal():
    second_number = e.get()
    s_num = float(second_number)
    e.delete(0, "end")

    global result
    if operator == "+":
        result = f_num + s_num
    elif operator == "-":
        result = f_num - s_num
    elif operator == "*":
        result = f_num * s_num
    elif operator == "/":
        result = f_num / s_num
    elif operator == "%":
        result = (f_num * 100) / s_num

    # rounding off the numbers
    s = str(int((s_num - (s_num % 1))))
    f = str(int((f_num - (f_num % 1))))
    x = int(min(len(f), len(s)))
    result = round(result, x)

    e.insert(0, result)


def button_clear():
    e.delete(0, "end")


# create a GUI window and set the title
root = tkinter.Tk()
root.title("Calculator")

# Entry Box
e = tkinter.Entry(root, width=12,)
e.grid(row=0, column=0, columnspan=4, pady=1, padx=5)
e.config(font=("Courier", 40), bd=0, highlightthickness=0)


# Define Buttons
button_1 = tkinter.Button(root, text="1", padx=18, pady=20, command=lambda: button_click(1), bd=0, highlightthickness=0,
                          bg="#999999", fg="black")
button_2 = tkinter.Button(root, text="2", padx=18, pady=20, command=lambda: button_click(2), bd=0, highlightthickness=0,
                          bg="#999999", fg="black")
button_3 = tkinter.Button(root, text="3", padx=18, pady=20, command=lambda: button_click(3), bd=0, highlightthickness=0,
                          bg="#999999", fg="black")
button_4 = tkinter.Button(root, text="4", padx=18, pady=20, command=lambda: button_click(4), bd=0, highlightthickness=0,
                          bg="#999999", fg="black")
button_5 = tkinter.Button(root, text="5", padx=18, pady=20, command=lambda: button_click(5), bd=0, highlightthickness=0,
                          bg="#999999", fg="black")
button_6 = tkinter.Button(root, text="6", padx=18, pady=20, command=lambda: button_click(6), bd=0, highlightthickness=0,
                          bg="#999999", fg="black")
button_7 = tkinter.Button(root, text="7", padx=18, pady=20, command=lambda: button_click(7), bd=0, highlightthickness=0,
                          bg="#999999", fg="black")
button_8 = tkinter.Button(root, text="8", padx=18, pady=20, command=lambda: button_click(8), bd=0, highlightthickness=0,
                          bg="#999999", fg="black")
button_9 = tkinter.Button(root, text="9", padx=18, pady=20, command=lambda: button_click(9), bd=0, highlightthickness=0,
                          bg="#999999", fg="black")
button_0 = tkinter.Button(root, text="0", padx=60, pady=20, command=lambda: button_click(0), bd=0, highlightthickness=0,
                          bg="#999999", fg="black")
button_point = tkinter.Button(root, text=".", padx=19.5, pady=20, command=button_point, bd=0, highlightthickness=0,
                              bg="#999999", fg="black")
button_divide = tkinter.Button(root, text="/", padx=18, pady=20, command=lambda: button_opp("/"), bd=0,
                               highlightthickness=0, bg="#f88104")
button_multiply = tkinter.Button(root, text="*", padx=18, pady=20, command=lambda: button_opp("*"), bd=0,
                                 highlightthickness=0, bg="#f88104")
button_minus = tkinter.Button(root, text="-", padx=18, pady=20, command=lambda: button_opp("-"), bd=0,
                              highlightthickness=0, bg="#f88104")
button_add = tkinter.Button(root, text="+", padx=18, pady=20, command=lambda: button_opp("+"), bd=0,
                            highlightthickness=0, bg="#f88104")
button_percent = tkinter.Button(root, text="%", padx=15, pady=20, command=lambda: button_opp("%"), bd=0,
                                highlightthickness=0)
button_sign = tkinter.Button(root, text="+/-", padx=13, pady=20, command=button_sign, bd=0, highlightthickness=0,
                             bg="#f88104")
button_equal = tkinter.Button(root, text="=", padx=18, pady=20, command=button_equal, bd=0, highlightthickness=0,
                              bg="#f88104")
button_clear = tkinter.Button(root, text="AC", padx=13, pady=20, command=button_clear, bd=0, highlightthickness=0)

# Put buttons on screen
button_clear.grid(row=1, column=0)
button_sign.grid(row=1, column=1)
button_percent.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_minus.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_0.grid(row=5, column=0, columnspan=2)
button_point.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

# start the GUI
root.mainloop()
