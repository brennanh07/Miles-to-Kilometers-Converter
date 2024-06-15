from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.geometry("300x150")
window.config(padx=40, pady=32)


def miles_to_km():
    miles = int(user_input.get())
    km = round(miles * 1.609, 2)
    km_label.config(text=km)


# User miles input
user_input = Entry(width=8, font=("Arial", 12))
user_input.grid(row=0, column=1)

# Miles label
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(row=0, column=2)

# Kilometers label
kilometers_label = Label(text="Km", font=("Arial", 12))
kilometers_label.grid(row=1, column=2)

equal_to = Label(text="is equal to", font=("Arial", 12))
equal_to.grid(row=1, column=0)

# Calculate button
calc_button = Button(text="Calculate", font=("Arial", 12), command=miles_to_km)
calc_button.grid(row=2, column=1)

# Result label
km_label = Label(text="", font=("Arial", 12))
km_label.grid(row=1, column=1)



window.mainloop()