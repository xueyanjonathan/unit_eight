import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")

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

root.mainloop()