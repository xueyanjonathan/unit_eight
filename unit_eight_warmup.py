import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")


def f_to_c():
    f_value = int(fahrenheitValue.get())
    c_value = 5 / 9 * (f_value - 32)
    celsiusValue.set(str(c_value))


fahrenheitValue = tkinter.StringVar()
celsiusValue = tkinter.StringVar()

fahrenheitLabel = tkinter.Label(root, text="degrees F:")
fahrenheitLabel.grid(row=1, column=1)

fahrenheitEntry = tkinter.Entry(root, textvariable=fahrenheitValue)
fahrenheitEntry.grid(row=1, column=2)

celsiusLabel = tkinter.Label(root, text="degrees C:")
celsiusLabel.grid(row=2, column=1)

celsiusAnswer = tkinter.Label(root, textvariable=celsiusValue)
celsiusAnswer.grid(row=2, column=2)

convertButton = tkinter.Button(root, text="Convert", command=f_to_c)
convertButton.grid(row=3, column=1)

root.mainloop()