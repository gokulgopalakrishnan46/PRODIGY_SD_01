import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def temperature_converter():
    temperature = float(entry.get())
    unit = var.get()

    if unit == 'Celsius':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        result.set(f"{temperature} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit and {kelvin:.2f} Kelvin.")
    elif unit == 'Fahrenheit':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        result.set(f"{temperature} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius and {kelvin:.2f} Kelvin.")
    elif unit == 'Kelvin':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        result.set(f"{temperature} Kelvin is equal to {celsius:.2f} degrees Celsius and {fahrenheit:.2f} degrees Fahrenheit.")
    else:
        result.set("Invalid unit of measurement. Please enter Celsius, Fahrenheit, or Kelvin.")

root = tk.Tk()
root.title("Temperature Converter")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

entry = ttk.Entry(frame, width=10)
entry.grid(row=0, column=0)

var = tk.StringVar()

option = ttk.OptionMenu(frame, var, "Celsius", "Fahrenheit", "Kelvin")
option.grid(row=0, column=1)

button = ttk.Button(frame, text="Convert", command=temperature_converter)
button.grid(row=0, column=2)

result = tk.StringVar()

label = ttk.Label(frame, textvariable=result)
label.grid(row=1, column=0, columnspan=3)

root.mainloop()