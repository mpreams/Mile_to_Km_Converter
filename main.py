from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=10, pady=10)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

kilometer_label = Label(text="Km")
kilometer_label.grid(row=1, column=2)

miles = Entry(width=15)
miles.grid(row=0, column=1)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

result = Label(text="0")
result.grid(row=1, column=1)


def convert():
    output = float(miles.get()) * 1.60934
    result.config(text=output)


calculate = Button(text="Calculate", command=convert)
calculate.grid(row=2, column=1)

window.mainloop()
