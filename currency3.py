#a simple currency converter using python

# importing the required libraries

import requests
import forex_python
from forex_python.converter import CurrencyRates
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# creating a window
win = tk.Tk()
win.title("Currency Converter")

# function to convert the currency
def convert():
    c = CurrencyRates()
    from_currency = currency1.get()
    to_currency = currency2.get()
    amount = float(entry1.get())
    new_amount = c.convert(from_currency, to_currency, amount)
    entry2.insert(0, str(new_amount))

# label and entry field
label1 = ttk.Label(win, text = "Enter amount")
label1.grid(row = 0, column = 0, padx = 5, pady = 5)
entry1 = ttk.Entry(win)
entry1.grid(row = 0, column = 1, padx = 5, pady = 5)

# label and entry field
label2 = ttk.Label(win, text = "Converted amount") 
label2.grid(row = 1, column = 0, padx = 5, pady = 5)
entry2 = ttk.Entry(win)
entry2.grid(row = 1, column = 1, padx = 5, pady = 5)

# label and entry field
label3 = ttk.Label(win, text = "From currency")
label3.grid(row = 2, column = 0, padx = 5, pady = 5)
entry3 = ttk.Entry(win)
entry3.grid(row = 2, column = 1, padx = 5, pady = 5)

# label and entry field
label4 = ttk.Label(win, text = "To currency")
label4.grid(row = 3, column = 0, padx = 5, pady = 5)
entry4 = ttk.Entry(win)
entry4.grid(row = 3, column = 1, padx = 5, pady = 5)

# button to call the convert function
button1 = ttk.Button(win, text = "Convert", command = convert)
button1.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5)

# dropdown
currency = CurrencyRates()
currency1 = ttk.Combobox(win, values = list(currency.get_rates("").keys()))
currency1.grid(row = 2, column = 1, padx = 5, pady = 5)
currency1.set("USD")
currency2 = ttk.Combobox(win, values = list(currency.get_rates("").keys()))
currency2.grid(row = 3, column = 1, padx = 5, pady = 5)
currency2.set("INR")

# infinite loop which can be terminated
# by keyboard or mouse interrupt
win.mainloop()

# End of code
# Output:
# The output window will look like this:
# Enter amount: [entry field]
# Converted amount: [entry field]
# From currency: [entry field]
# To currency: [entry field]
# Convert
# [dropdown] [dropdown]
# The user can enter the amount, select the currencies, and click on the convert button to get the converted amount.
# The user can also select the currencies from the dropdown menu.
# The user can also terminate the window using the keyboard or mouse interrupt.
# The user will get the converted amount in the output window.