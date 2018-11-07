import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")

fahrenheitLabel = tkinter.Label(root, text = "degrees F:")
fahrenheitLabel.grid(row=1, column=1)

fahrenheitEntry = tkinter.Entry(root)
fahrenheitEntry.grid(row=1, column=2)

celciusLabel = tkinter.Label(root, text = "degrees C:")
celciusLabel.grid(row=2, column=1)

root.mainloop()