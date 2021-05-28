from tkinter import *

window = Tk()
window.title("miles to kilometer converter")
window.config(padx=20, pady=20)


def converter():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    convert_miles_to_km_label.config(text=f"{km}")


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Mile")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="Is Equal To")
is_equal_to_label.grid(column=0, row=1)

convert_miles_to_km_label = Label(text="0")
convert_miles_to_km_label.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=converter)
calculate_button.grid(column=1, row=2)

window.mainloop()
