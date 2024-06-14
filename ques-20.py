lst = []
n = int(input("Enter the range of list: "))
for i in range(n):
  elm = int(input("Enter the number :"))
  lst.append(elm)
print("List of the numbers: ",lst)

sum =0
for i in lst:
  sum += i
print("Sum of all numbers present in list: ",sum)
