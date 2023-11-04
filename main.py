from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)
miles_entry.insert(END, string="0")

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate")
calc_button.grid(column=1, row=2)

window.mainloop()
