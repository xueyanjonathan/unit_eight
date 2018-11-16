# 11/16/2018
# Jonathan Lin
# GUI Calculator
# Using GUI to create a calculator which can execute addition, subtraction, multiplication, division,
# square, percentage, and clear.

import tkinter

root = tkinter.Tk()  # Create a root window which everything will be in
root.title("Jonathan's calculator")  # The title of the window


def one():
    """
    Put a string 1 in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "1")


def two():
    """
    Put a string 2 in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "2")


def three():
    """
    Put a string 3 in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "3")


def four():
    """
    Put a string 4 in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "4")


def five():
    """
    Put a string 5 in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "5")


def six():
    """
    Put a string 6 in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "6")


def seven():
    """
    Put a string 7 in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "7")


def eight():
    """
    Put a string 8 in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "8")


def nine():
    """
    Put a string 9 in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "9")


def zero():
    """
    Put a string 0 in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "0")


def add():
    """
    Put a string plus sign in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "+")


def subtract():
    """
    Put a string minus sign in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "-")


def divide():
    """
    Put a string division sign in the entry field.
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + "/")


def multiply():
    """
    Put a string multiplication sign in the entry field.
    :return: Nothing
    """

    answer = result.get()
    result.set(answer + "*")


def x_square():
    """
    Turn the string number in the entry field into a float, square it, and then turn it back to a string.
    :return: Nothing
    """
    answer = result.get()
    result.set(str(float(answer) ** 2))


def percentage():
    """
    Turn the string number in the entry field into a float, divide it by 100, and then turn it back to a string.
    :return: Nothing
    """
    answer = result.get()
    result.set(str(float(answer) / 100))


def point():
    """
    Put a string desmos point in the entry field
    :return: Nothing
    """
    answer = result.get()
    result.set(answer + ".")


def all_clear():
    """
    Clear the entry field by setting the result into blank
    :return: Nothing
    """
    result.set("")


def evaluate():
    """
    Calculate the result by using the eval function
    :return: Nothing 
    """
    result.set(eval(result.get()))


result = tkinter.StringVar()  # Result variable shown in the entry field

calculatorLabel = tkinter.Label(root, text="Jonathan's Super Calculator", font="HarryP 24 bold")
# Create a title in the root window with the name and font above
calculatorLabel.grid(row=1, column=1, columnspan=4)  # Place the title at row 1 column 1

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
