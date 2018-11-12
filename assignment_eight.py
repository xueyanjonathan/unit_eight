import tkinter

root = tkinter.Tk()
root.title("Jonathan's calculator")


def one():
    one = result.get()
    result.set(one + "1")


def two():
    two = result.get()
    result.set(two + "2")


def three():
    three = result.get()
    result.set(three + "3")


def four():
    four = result.get()
    result.set(four + "4")


def five():
    five = result.get()
    result.set(five + "5")


def six():
    six = result.get()
    result.set(six + "6")


def seven():
    seven = result.get()
    result.set(seven + "7")


def eight():
    eight = result.get()
    result.set(eight + "8")


def nine():
    nine = result.get()
    result.set(nine + "9")


def zero():
    zero = result.get()
    result.set(zero + "0")


def addition():
    x = result.get()
    y = result.get()
    answer = float(x) + float(y)
    result.set(answer)


result = tkinter.StringVar()

calculatorEntry = tkinter.Entry(root, textvariable=result)
calculatorEntry.grid(row=1, column=1, columnspan=4)

allclear = tkinter.Button(root, text="AC")
allclear.grid(row=2, column=1)

square = tkinter.Button(root, text="x²")
square.grid(row=2, column=2)

percent = tkinter.Button(root, text="%")
percent.grid(row=2, column=3)

division = tkinter.Button(root, text="÷")
division.grid(row=2, column=4)

number_one = tkinter.Button(root, text="1", command=one)
number_one.grid(row=3, column=1)

number_two = tkinter.Button(root, text="2", command=two)
number_two.grid(row=3, column=2)

number_three = tkinter.Button(root, text="3", command=three)
number_three.grid(row=3, column=3)

multiplication = tkinter.Button(root, text="×")
multiplication.grid(row=3, column=4)

number_four = tkinter.Button(root, text="4", command=four)
number_four.grid(row=4, column=1)

number_five = tkinter.Button(root, text="5", command=five)
number_five.grid(row=4, column=2)

number_six = tkinter.Button(root, text="6", command=six)
number_six.grid(row=4, column=3)

addition = tkinter.Button(root, text="+", command=addition)
addition.grid(row=4, column=4)

number_seven = tkinter.Button(root, text="7", command=seven)
number_seven.grid(row=5, column=1)

number_eight = tkinter.Button(root, text="8", command=eight)
number_eight.grid(row=5, column=2)

number_nine = tkinter.Button(root, text="9", command=nine)
number_nine.grid(row=5, column=3)

subtraction = tkinter.Button(root, text="-")
subtraction.grid(row=5, column=4)

desmospoint = tkinter.Button(root, text=".")
desmospoint.grid(row=6, column=1)

number_zero = tkinter.Button(root, text="0", command=zero)
number_zero.grid(row=6, column=2)

equal = tkinter.Button(root, text="=")
equal.grid(row=6, column=4)

root.mainloop()