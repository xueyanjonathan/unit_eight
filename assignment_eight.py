import tkinter

root = tkinter.Tk()
root.title("Jonathan's calculator")

result = tkinter.StringVar()

calculatorEntry = tkinter.Entry(root, textvariable=result)
calculatorEntry.grid(row=1, column=1)

allclear = tkinter.Button(root, text="AC")
allclear.grid(row=2, column=1)

square = tkinter.Button(root, text="x²")
square.grid(row=2, column=2)

percent = tkinter.Button(root, text="%")
percent.grid(row=2, column=3)

division = tkinter.Button(root, text="÷")
division.grid(row=2, column=4)

number_one = tkinter.Button(root, text="1")
number_one.grid(row=3, column=1)

number_two = tkinter.Button(root, text="2")
number_two.grid(row=3, column=2)

number_three = tkinter.Button(root, text="3")
number_three.grid(row=3, column=3)

multiplication = tkinter.Button(root, text="×")
multiplication.grid(row=3, column=4)

number_four = tkinter.Button(root, text="4")
number_four.grid(row=4, column=1)

number_five = tkinter.Button(root, text="5")
number_five.grid(row=4, column=2)

number_six = tkinter.Button(root, text="6")
number_six.grid(row=4, column=3)

addition = tkinter.Button(root, text="+")
addition.grid(row=4, column=4)

number_seven = tkinter.Button(root, text="7")
number_seven.grid(row=5, column=1)

number_eight = tkinter.Button(root, text="8")
number_eight.grid(row=5, column=2)

number_nine = tkinter.Button(root, text="9")
number_nine.grid(row=5, column=3)

subtraction = tkinter.Button(root, text="-")
subtraction.grid(row=5, column=4)

desmospoint = tkinter.Button(root, text=".")
desmospoint.grid(row=6, column=1)

number_zero = tkinter.Button(root, text="0")
number_zero.grid(row=6, column=2)

equal = tkinter.Button(root, text="=")
equal.grid(row=6, column=4)

root.mainloop()