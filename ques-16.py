userInput= input("enter the string: ")
 

count ={}

for i in userInput:
  if i in count:
    count[i] += 1
  else:
    count[i] = 1

print("Frequency of each element:\n")
for i,freq in count.items():
 print(f" '{i}':{freq}")