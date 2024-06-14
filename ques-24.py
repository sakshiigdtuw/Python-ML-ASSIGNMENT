num1 = int(input("Enter the number1:  "))
num2 = int(input("Enter the number2:  "))

operator = input("Enter the operator: ")

if operator == "+":
  add = num1 + num2
  print("Addition of two numbers : ",add) 
elif operator == "-":
  subtract = num1 - num2
  print("subtraction of two numbers : ",subtract) 

elif operator == "*":
  product = num1 * num2
  print("Multiplication of two numbers : ",product) 

elif operator == "/":
  division = num1 / num2
  print("Division of two numbers : ",division) 

else:
  print("You have entered wrong operator: ")
