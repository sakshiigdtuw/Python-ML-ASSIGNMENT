
given =  input("Enter the  present Temperature in celsius or fahrenheit ")


if given == "celsius":
  celsius = int(input("enter temperature in Celsius: "))
  fahrenheit = celsius*9/5 + 32
  print("Temperature in Fahrenheit:  ",fahrenheit)

elif given == "fahrenheit":
  fahrenheit = int(input("enter temperature in Fahrenheit : "))
  celsius = fahrenheit*5/9 - 32
  print("Temperature in Celsius: ",celsius)
else: 
  print("Type of Temperature is not relevant.Try Again.")