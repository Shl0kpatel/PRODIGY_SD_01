print("User guide: Enter the temperature value and unit (Please use Celsius (C), Fahrenheit (F), or Kelvin (K)).")
print("For example if you want to enter 25 degrees Celsius then enter 25 C or 25 Celsius")
user_input = input("Enter the temperature value and unit : ")

try:
  temp, unit = user_input.split(" ")
  temp = float(temp)  # Convert temperature to float
  unit = unit.lower()  # Convert unit to lowercase
except ValueError:
  print("Invalid input format. Please enter a number followed by a unit (e.g., Celsius, Fahrenheit, Kelvin).")
  exit()

if unit == "celsius" or unit == "c":
  # Convert Celsius to Fahrenheit and Kelvin
  k = temp - 273.15
  f = (temp * 9/5) + 32
  print("Temperature in Kelvin is:", "{:.2f}".format(k))
  print("Temperature in Fahrenheit is:", "{:.2f}".format(f))
  
elif unit == "fahrenheit" or unit == "f":
  # Convert Fahrenheit to Celsius and Kelvin
  c = (temp - 32) * 5/9
  k = c - 273.15
  print("Temperature in Celsius is:", "{:.2f}".format(c))
  print("Temperature in Kelvin is:", "{:.2f}".format(k))
  
elif unit == "kelvin" or unit == "k":
  # Convert Kelvin to Celsius and Fahrenheit
  c = temp - 273.15
  f = (c * 9/5) + 32
  print("Temperature in Celsius is:", "{:.2f}".format(c))
  print("Temperature in Fahrenheit is:", "{:.2f}".format(f))
  
else:
  print("Invalid unit. Please use Celsius (C), Fahrenheit (F), or Kelvin (K).")

