
def factorial(number):
  if number==0 | number==1:
    return 1
  else:
    return number * factorial(number-1)
  
number = int(input("Enetr the number: "))
result =  factorial(number)
print("Fcatorial of number: ",result)