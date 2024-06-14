def fibonacci(n):
  if n<0:
    return None
  elif n==0:
    return 0
  elif n==1:
    return 1
  else:
    a=0
    b=1
    for i in range(n):
      c = a + b
      a , b = b , c
    return c
    
n = int(input("Enter the range for fibonacci series: "))
for i in range(n):
  series = fibonacci(i)
  print(series)