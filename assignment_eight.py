import tkinter

root = tkinter.Tk()
root.title("Jonathan's calculator")


def one():
    answer = result.get()
    result.set(answer + "1")


def two():
    answer = result.get()
    result.set(answer + "2")


def three():
    answer = result.get()
    result.set(answer + "3")


def four():
    answer = result.get()
    result.set(answer + "4")


def five():
    answer = result.get()
    result.set(answer + "5")


def six():
    answer = result.get()
    result.set(answer + "6")


def seven():
    answer = result.get()
    result.set(answer + "7")


def eight():
    answer = result.get()
    result.set(answer + "8")


def nine():
    answer = result.get()
    result.set(answer + "9")


def zero():
    answer = result.get()
    result.set(answer + "0")


def add():
    answer = result.get()
    result.set(answer + "+")


def subtract():
    answer = result.get()
    result.set(answer + "-")


def divide():
    answer = result.get()
    result.set(answer + "/")


def multiply():
    answer = result.get()
    result.set(answer + "*")


def x_square():
    answer = result.get()
    result.set(str(float(answer) ** 2))


def percentage():
    answer = result.get()
    result.set(str(float(answer) / 100))


def point():
    answer = result.get()
    result.set(answer + ".")


def all_clear():
    result.set("")


def evaluate():
    result.set(eval(result.get()))


result = tkinter.StringVar()

calculatorLabel = tkinter.Label(root, text="Jonathan's Super Calculator", font="Verdana 20")
calculatorLabel.grid(row=1, column=1, columnspan=4)

calculatorEntry = tkinter.Entry(root, textvariable=result)
calculatorEntry.grid(row=2, column=1, columnspan=4)

allclear = tkinter.Button(root, text="AC", command=all_clear)
allclear.grid(row=3, column=1)

square = tkinter.Button(root, text="x²", command=x_square)
square.grid(row=3, column=2)

percent = tkinter.Button(root, text="%", command=percentage)
percent.grid(row=3, column=3)

division = tkinter.Button(root, text="÷", command=divide)
division.grid(row=3, column=4)

number_one = tkinter.Button(root, text="1", command=one)
number_one.grid(row=4, column=1)

number_two = tkinter.Button(root, text="2", command=two)
number_two.grid(row=4, column=2)

number_three = tkinter.Button(root, text="3", command=three)
number_three.grid(row=4, column=3)

multiplication = tkinter.Button(root, text="×", command=multiply)
multiplication.grid(row=4, column=4)

number_four = tkinter.Button(root, text="4", command=four)
number_four.grid(row=5, column=1)

number_five = tkinter.Button(root, text="5", command=five)
number_five.grid(row=5, column=2)

number_six = tkinter.Button(root, text="6", command=six)
number_six.grid(row=5, column=3)

addition = tkinter.Button(root, text="+", command=add)
addition.grid(row=5, column=4)

number_seven = tkinter.Button(root, text="7", command=seven)
number_seven.grid(row=6, column=1)

number_eight = tkinter.Button(root, text="8", command=eight)
number_eight.grid(row=6, column=2)

number_nine = tkinter.Button(root, text="9", command=nine)
number_nine.grid(row=6, column=3)

subtraction = tkinter.Button(root, text="-", command=subtract)
subtraction.grid(row=6, column=4)

desmosPoint = tkinter.Button(root, text=".", command=point)
desmosPoint.grid(row=7, column=1)

number_zero = tkinter.Button(root, text="0", command=zero)
number_zero.grid(row=7, column=2)

equal = tkinter.Button(root, text="=", command=evaluate)
equal.grid(row=7, column=4)

root.mainloop()
